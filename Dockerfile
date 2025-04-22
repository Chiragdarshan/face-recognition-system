# Use an official Python runtime
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DEFAULT_TIMEOUT=300

# Install system dependencies for Tkinter, OpenCV, and other required libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    xvfb \
    tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Upgrade pip and install Python dependencies with long timeout
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --timeout=300 -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Default command to run the Flask app
CMD ["flask", "run"]
