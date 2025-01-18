# Use an official Python runtime as a parent image
FROM python:3.9-alpine


RUN pip install pg8000
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app

COPY game.py /app

# Run the Tic Tac Toe game
CMD ["python", "game.py"]