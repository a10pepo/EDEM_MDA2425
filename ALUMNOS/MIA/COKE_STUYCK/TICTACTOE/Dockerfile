# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install requirements
RUN pip3 install -r requirements.txt

# Run the Tic Tac Toe game
CMD ["python3", "game.py"]