from loaders.log_loader import LogLoader
from loaders.pdf_loader import PDFLoader
from loaders.markdown_loader import MarkdownLoader
from loaders.text_loader import TextLoader


class LoaderFactory:

    LOADERS = {

        ".pdf": PDFLoader(),

        ".md": MarkdownLoader(),

        ".txt": TextLoader(),
        
        ".log": LogLoader()

    }

    @classmethod
    def get_loader(cls, extension):

        return cls.LOADERS.get(extension.lower())