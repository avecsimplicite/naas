FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

# Copy app files
COPY . /app

# Install Python dependencies
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Use gunicorn to serve the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2", "--threads", "4"]
