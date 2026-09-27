from pathlib import Path

# This class is responsible for parsing log files and extracting important information such as errors and warnings. It reads the log file line by line, checks for lines containing "ERROR" or "WARNING", and collects those lines into a list. The extracted information is then returned as a structured dictionary containing the text, source, category, technology, document type, and file path of the log file.
class LogParser:

    def parse(self, log_file: Path):

        with open(log_file, "r") as file:

            lines = file.readlines()
            important_lines = []

        for line in lines:

            if "ERROR" in line:

                important_lines.append(line.strip())

            elif "WARNING" in line:

                important_lines.append(line.strip())
            
        return {

    "text": "\n".join(important_lines),

    "source": log_file.name,

    "category": "logs",

    "technology": "kubernetes",

    "document_type": "log",

    "filepath": str(log_file)

}