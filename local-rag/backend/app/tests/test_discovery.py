from pathlib import Path

from discovery.document_discovery import DocumentDiscovery

knowledge = Path("../../knowledge")

service = DocumentDiscovery()

files = service.discover(knowledge)

print(f"Found {len(files)} files\n")

for file in files:

    print(file)