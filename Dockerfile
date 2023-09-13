# Use the official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./requirements.txt

# Remove the virtual environment (if used)
rm -rf /home/adminuser/venv

# Remove cached files
rm -rf ~/.cache/pip



# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

COPY . /app



# Define environment variable
# ENV APP_LOG_LEVEL "ERROR"
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get update && apt-get install -y libgl1-mesa-glx


# Run your Python application
CMD streamlit run app.py --server.port 8080 --server.enableCORS false 