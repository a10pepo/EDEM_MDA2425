# Use an official Python runtime as a parent image
FROM python:3.12

COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY game.py /app

# Run the Tic Tac Toe game
CMD ["python3", "game.py"]