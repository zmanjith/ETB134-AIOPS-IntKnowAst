from enum import Enum


class DocumentType(str, Enum):

    PDF = "pdf"

    MARKDOWN = "markdown"

    TEXT = "text"

    LOG = "log"

    ALERT = "alert"

    K8S_EVENT = "k8s_event"

    RUNBOOK = "runbook"

    RCA = "rca"