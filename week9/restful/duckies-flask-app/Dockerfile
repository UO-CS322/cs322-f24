FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and application files
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]

# Expose the application port
EXPOSE 5005
