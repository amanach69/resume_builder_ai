# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies
RUN apt update && apt install -y gcc

# Set environment variables
ENV USER_AGENT=ResumeBuilder/1.0

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p logs

# Run the app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]
