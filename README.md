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

## Usage

- Place image files in the `images/` directory on your host machine.
- The server will serve any file requested at the root path.
- If the file doesn't exist, it returns a 404 error.

## Troubleshooting

- Ensure the `images/` directory exists and contains the desired files.
- Check that port 5000 is not in use.
- For production, consider using a more robust web server like Nginx.