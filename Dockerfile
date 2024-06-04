# Use the official lightweight Python image.
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for streamlit
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "vision.py"]
