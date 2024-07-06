# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Flask and other dependencies
RUN pip install --no-cache-dir Flask Flask-Cors pandas requests

# Expose the Flask port
EXPOSE 5000

# Define environment variable for SQLite database
ENV DATABASE_URI="sqlite:///game_data.db"

# Command to run the Flask application
CMD ["python", "./app.py"]
