# Use the official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8501

COPY . /app

# Define environment variable
# ENV APP_LOG_LEVEL "ERROR"

# Run your Python application
CMD ["app.py"]
