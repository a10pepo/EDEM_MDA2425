# Usage instructions:
# docker build -t fast-api-server .
# docker run -p 8080:8080 fast-api-server

# Use the latest version of the Ubuntu base image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app

COPY requirements.txt /app

# Install the application dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app /app
COPY model.pkl /app 

# Expose port 8080
EXPOSE 8080

# Run the application with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
