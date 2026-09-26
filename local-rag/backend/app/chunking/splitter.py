from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentSplitter:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        
# splits a single document into chunks, each chunk is a dictionary with the same metadata as the original document, plus a "chunk" key indicating the chunk number
    def split(self, document):
        text = document.get(
                "searchable_text",
                document["text"]
            )
        text_chunks = self.splitter.split_text(text)
        # text_chunks = self.splitter.split_text(document["text"])

        chunk_documents = []

        for chunk_number, text in enumerate(text_chunks, start=1):
            chunk_metadata = document["metadata"].copy()

            chunk_metadata["page"] = document["page"]
            chunk_metadata["chunk"] = chunk_number

            chunk_documents.append(
                {
                    "chunk_id": (  
                                    f"{document['category']}/"
                                    f"{document['source']}:"
                                    f"p{document['page']}:"
                                    f"c{chunk_number}"
                                ),
                    "text": text,
                    "metadata": chunk_metadata,
                    "filepath": document["filepath"]
                }
            )
           

        return chunk_documents
    
    
    # each document is split into chunks, and all chunks are collected into a single list
    def split_documents(self, documents):

        all_chunks = []

        for document in documents:
            chunks = self.split(document)
            all_chunks.extend(chunks)
        return all_chunks