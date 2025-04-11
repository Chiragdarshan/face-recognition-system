FROM python:3.12.3-slim-bookworm

# Avoid creating .pyc files and keep logs visible
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    libgl1-mesa-glx \
    python3-opencv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy all code
COPY . /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run your app (update if your main script is different)
CMD ["python", "student.py"]
