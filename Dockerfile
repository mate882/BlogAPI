# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project
COPY . .

# Expose port
EXPOSE 8000

# Run Gunicorn instead of runserver
CMD ["gunicorn", "Blog.wsgi:application", "--bind", "0.0.0.0:8000"]
