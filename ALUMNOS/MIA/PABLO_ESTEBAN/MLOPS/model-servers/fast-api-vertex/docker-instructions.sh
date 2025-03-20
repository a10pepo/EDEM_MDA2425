#!/bin/bash

# Set environment variables
export AIP_HEALTH_ROUTE="/health"
export AIP_PREDICT_ROUTE="/predict"
export AIP_PORT=8080

# Build the Docker image
docker build -t fastapi-app-vertex .

# Run the Docker container with environment variables
docker run -p 8080:8080 \
    -e AIP_HEALTH_ROUTE="$AIP_HEALTH_ROUTE" \
    -e AIP_PREDICT_ROUTE="$AIP_PREDICT_ROUTE" \
    -e AIP_PORT="$AIP_PORT" \
    fastapi-app-vertex