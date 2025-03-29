#!/bin/bash

# gcloud auth login
# gcloud auth configure-docker
# gcloud config set project YOUR_PROJECT_ID
# gcloud services enable artifactregistry.googleapis.com aiplatform.googleapis.com

# === CONFIGURABLE VARIABLES ===
PROJECT_ID="your-project-id"  # Replace with your Google Cloud project ID
REGION="us-central1"  # Change if deploying to a different region
REPO_NAME="vertex-repo"  # Artifact Registry repository name
IMAGE_NAME="fastapi-app-vertex"
TAG="latest"

# === BUILD & TAG DOCKER IMAGE ===
echo "Building Docker image..."
docker build -t ${IMAGE_NAME}:${TAG} .

# Authenticate Docker to Google Cloud
#echo "Authenticating with Google Cloud..."
#gcloud auth configure-docker ${REGION}-docker.pkg.dev

# Tag image for Artifact Registry (recommended)
IMAGE_URI="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${TAG}"
echo "Tagging image as: ${IMAGE_URI}"
docker tag ${IMAGE_NAME}:${TAG} ${IMAGE_URI}

# Push image to Artifact Registry
echo "Pushing image to Google Cloud Artifact Registry..."
docker push ${IMAGE_URI}