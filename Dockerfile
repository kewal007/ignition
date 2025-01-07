# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and switch to a non-root user
RUN useradd -m myuser
USER myuser

# Install Python dependencies
COPY --chown=myuser:myuser requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=myuser:myuser . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ignition.wsgi"]
