from enum import Enum


class Technology(str, Enum):

    GENERAL = "general"

    KUBERNETES = "kubernetes"

    DOCKER = "docker"

    POSTGRESQL = "postgresql"

    PROMETHEUS = "prometheus"

    LOKI = "loki"

    GRAFANA = "grafana"