from LLM.ollama_service import OllamaService


class LogSummarizer:

    def __init__(self):

        self.llm = OllamaService()
        
    def _build_prompt(self, document):
        prompt = f"""
            You are an experienced Site Reliability Engineer.

            Analyze the following application log.

            Identify:

            1. The primary operational problem.

            2. The likely root cause.

            3. The affected component.

            4. Any repeated failures.

            Write a concise operational summary.

            Application Log

            {document["text"]}

            """
        return prompt
    
    def summarize(self, document):
        prompt = self._build_prompt(document)
        summary = self.llm.generate(prompt)
        document["analysis"] = {
            "summary": summary,
            "root_cause": None,
            "confidence": None
        }

        document["searchable_text"] = f"""

        Document_Type: {document["document_type"]}
        Technology: {document["technology"]}
        Source: {document["source"]}
                
        Operational Summary
        ===================

        {summary}

        ===================
        Key Events
        ===================

        {document["text"]}
        """
        return document