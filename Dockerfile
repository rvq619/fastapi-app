
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables (adjust as needed)
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . /app/

# Create a directory for uploaded files and declare it as a volume
RUN mkdir -p /app/uploads
VOLUME ["/app/uploads"]

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


