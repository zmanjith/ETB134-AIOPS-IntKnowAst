from pathlib import Path

from operational_inputs.log_parser import LogParser
from operational_inputs.log_summarizer import LogSummarizer

parser = LogParser()

document = parser.parse(

    Path("../../knowledge/logs/payment-service.log")

)

summarizer = LogSummarizer()

summary_document = summarizer.summarize(document)
print(summary_document)
