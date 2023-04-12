# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster
FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget
RUN apt-get update && apt-get install -y gnupg


RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install the required packages
RUN apt-get update && apt-get install -y \
    mongodb-org \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN systemctl start mongod


# Make port 5000 available to the world outside this container
EXPOSE 5000
EXPOSE 27017


# Set the environment variable for MongoDB
ENV MONGO_URL mongodb://localhost:27017/

# Run app.py when the container launches
CMD ["python", "app.py"]
