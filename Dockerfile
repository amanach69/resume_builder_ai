# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Run the app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]
