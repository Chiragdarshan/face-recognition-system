# Use an official Python runtime
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy everything into the container
COPY . /app

# Install dependencies

RUN pip install --upgrade pip &&  \
    pip install --timeout=300 -r requirements.txt


# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "student.py"]
