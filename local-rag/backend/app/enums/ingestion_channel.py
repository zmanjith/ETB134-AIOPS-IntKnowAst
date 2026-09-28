from enum import Enum

## Answer to the question: "Where are getting these inputs from?" is that these are the ingestion channels for the operational documents. The ingestion channels are defined in the IngestionChannel enum class, which includes STATIC_KNOWLEDGE, LIVE_SIGNAL, and USER_QUERY. These channels represent different sources or methods through which operational documents can be ingested into the system.
class IngestionChannel(str, Enum):
    STATIC_KNOWLEDGE = "static_knowledge"
    LIVE_SIGNAL = "live_signal"
    USER_QUERY = "user_query"
    