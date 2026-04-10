# Docker Image Server

A simple Dockerized web server that serves images from a mounted volume.

## Setup

1. Create an `images/` directory in the project root and place your image files there.
2. Build the Docker image:

   ```
   docker build -t image-server .
   ```
3. Run the container with the volume mounted:

   ```
   docker run -v $(pwd)/images:/images -p 5000:5000 image-server
   ```
4. Access images via: `http://localhost:5000/your-image.jpg`

## Production Deployment

The container uses Gunicorn as a production WSGI server instead of Flask's development server, making it suitable for production use.
