# Use an official Python runtime
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for Tkinter, OpenCV, and other required libraries
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set work directory inside the container
WORKDIR /app

# Copy everything into the container (including all project files)
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && \
    pip install --timeout=300 -r requirements.txt

# Expose the port Flask runs on (if Flask app is being used in the project)
EXPOSE 5000

# Default command to run your student.py script
CMD ["python", "student.py"]
