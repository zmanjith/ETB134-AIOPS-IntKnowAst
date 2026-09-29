from enums.category import Category
from enums.document_type import DocumentType
from enums.severity import Severity
from enums.technology import Technology
from enums.ingestion_channel import IngestionChannel
from kubernetes import client
from kubernetes import config
from kubernetes import watch
from models.knowledge_unit import KnowledgeUnit
from enums.ingestion_channel import IngestionChannel


class KubernetesEventWatcher:
    
    def __init__(self):
        
        config.load_kube_config()  # Load the Kubernetes configuration from the default location
        
        self.v1 = client.CoreV1Api()  # Create an instance of the CoreV1Api to interact with Kubernetes resources
        
    def watch_events(self):

        watcher = watch.Watch()

        for event in watcher.stream(
                self.v1.list_event_for_all_namespaces
        ):

            yield self._convert_event(event["object"])
    
    
    def _convert_event(self, event):

        if event.type != "Warning":
            return None

        return KnowledgeUnit(

            text=event.message,

            source="kubernetes",

            category=Category.KUBERNETES,

            document_type=DocumentType.K8S_EVENT,

            technology=Technology.KUBERNETES,

            severity=Severity.WARNING,
            
            ingestion_channel=IngestionChannel.LIVE_SIGNAL,

            timestamp=str(event.last_timestamp),

            namespace=event.metadata.namespace,

            labels={
                "reason": event.reason,
                "object": event.involved_object.name
            }

        )