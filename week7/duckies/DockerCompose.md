# Docker Compose

To create a `docker-compose.yml` file that includes both a Flask web application and MongoDB database as services, you will follow a process similar to these steps. Here's a simple example setup:

### Step 1: Create Dockerfile for the Flask Application

In your project directory, create a file named `Dockerfile` with the following content:


```Dockerfile
# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and application files
COPY requirements.txt ./
COPY app.py ./
COPY templates/ ./templates/

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]

# Expose the application port
EXPOSE 5005
```

### Step 2: Create `requirements.txt`

Create a `requirements.txt` file in the same directory with the following content:


```
Flask
Flask-Cors
pymongo
```

### Step 3: Create `docker-compose.yml`

In the same project directory, create a `docker-compose.yml` file with the following content:


```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5005:5005"  # Expose port 5005
    depends_on:
      - db
    environment:
      - MONGO_URI=mongodb://db:27017/DuckyCollection  # Connect to MongoDB service

  db:
    image: mongo:latest # Use the official MongoDB image
    ports:
      - "27017:27017"  # Optional: expose MongoDB port 27017
```

### Step 4: Edit Flask Application to Use Environment Variables

You will need to modify your Flask app to utilize the environment variable `MONGO_URI`. Update your `app.py` file's MongoDB connection line as follows:


```python
import os

# Connect to MongoDB using the ENV variable
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/DuckyCollection')
client = MongoClient(mongo_uri)
```

### Step 5: Build and Run the Containers

In your terminal, navigate to your project directory (where the `docker-compose.yml` file is located) and run:


```bash
docker-compose up --build
```

This command will:

1. Build the Flask application image based on the provided Dockerfile.
2. Pull the MongoDB image if it isn't already available.
3. Create and start both the `web` and `db` services.

### Step 6: Access the Web Application

Once the containers are running, you should be able to access your Flask web application at `http://localhost:5005`.


In the above docker compose setup, the `web` service runs the Flask app, which connects to the MongoDB database service (`db`).
