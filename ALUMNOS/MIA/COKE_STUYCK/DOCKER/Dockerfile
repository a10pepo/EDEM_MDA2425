# Use an official and slim Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY script/sum_two_numbers.py /app/sum_two_numbers.py

# Set the default command to run the Python script with arguments
ENTRYPOINT ["python3", "sum_two_numbers.py"]