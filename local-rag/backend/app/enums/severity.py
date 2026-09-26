from enum import Enum


class Severity(str, Enum):

    INFO = "info"

    WARNING = "warning"

    ERROR = "error"

    CRITICAL = "critical"