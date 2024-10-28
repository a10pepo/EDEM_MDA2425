# Use a slim version of the Python 3.9 image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY ahorcado.py ./

# Copy the words file into the container
COPY palabras.txt ./

# Uncomment the line below if you have dependencies listed in a requirements.txt file
# RUN pip install -r requirements.txt

# Set the default command to run when the container starts
# This allows passing an argument (the words file) when running the container
CMD ["python", "ahorcado.py", "palabras.txt"]
