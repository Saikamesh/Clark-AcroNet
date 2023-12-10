# Base image
FROM python:3.11-bullseye 

# To debug python code in docker
ENV PYTHONUNBUFFERED = 1 

# Set working directory in container
WORKDIR /app

# Copy requirements.txt to /app/requirements.txt
COPY requirements.txt requirements.txt

# Install requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
