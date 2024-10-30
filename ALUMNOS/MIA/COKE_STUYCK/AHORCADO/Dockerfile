# Use a slim version of the Python 3.9 image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required packages
RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY ahorcado.py ./

# Set the entrypoint to allow arguments to be passed directly to the script
ENTRYPOINT ["python", "ahorcado.py"]