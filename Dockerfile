FROM python:3.9-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install gunicorn && \
    pip install -r requirements.txt

# Copy project
COPY . /app/

# Create a user to run your app
RUN adduser --disabled-password --gecos '' myuser
USER myuser

EXPOSE 8000

# Start gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]
