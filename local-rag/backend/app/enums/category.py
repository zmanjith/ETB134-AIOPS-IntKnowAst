from enum import Enum


class Category(str, Enum):

    DOCUMENTATION = "documentation"

    LOGS = "logs"

    ALERTS = "alerts"

    KUBERNETES = "kubernetes"

    INCIDENTS = "incidents"

    METRICS = "metrics"