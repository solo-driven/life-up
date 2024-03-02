# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements file
COPY api_requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r api_requirements.txt

# Copy other files 
COPY api.py app.py autoencoder_model.h5 scaler.pkl /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to improve Python logging (optional)
ENV PYTHONUNBUFFERED=1

# Run api.py when the container launches
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]