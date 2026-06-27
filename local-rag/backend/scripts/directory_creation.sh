#!/bin/bash

# Define the base directory
BASE_DIR="knowledge"

# List of subdirectories to create
SUBDIRS=(
    "kubernetes"
    "docker"
    "terraform"
    "aws"
    "linux"
    "monitoring"
    "incidents"
    "runbooks"
    "rca"
    "architecture"
)

# Create directories
for dir in "${SUBDIRS[@]}"; do
    mkdir -p "$BASE_DIR/$dir"
done

echo "Folder structure created successfully under ./$BASE_DIR"
