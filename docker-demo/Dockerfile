# Base image
FROM python:3.9 
# Use an official Python runtime as a parent image

# Set the working directory in the container
WORKDIR /main 
# Set the working directory in the container

# Copy the current directory contents into the container at /main
COPY . /main

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000 
# Expose port 5000 to the outside world

# Command to run the application
CMD ["python", "./main.py"]
