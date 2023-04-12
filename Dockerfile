Copy code
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app/app.py

# Install the required packages
RUN apt-get update && apt-get install -y \
    mongodb \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the environment variable for MongoDB
ENV MONGO_URL mongodb://localhost:27017/

# Run app.py when the container launches
CMD ["python", "app.py"]
