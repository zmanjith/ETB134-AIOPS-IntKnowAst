from pathlib import Path

from operational_inputs.log_parser import LogParser

parser = LogParser()

document = parser.parse(

    Path("../../knowledge/logs/payment-service.log")

)

print(document)