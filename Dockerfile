# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py

# Run flask command to start the application
CMD ["flask", "run", "--host=0.0.0.0"]
