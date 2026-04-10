from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_image(filename):
    if os.path.exists(os.path.join('/images', filename)):
        return send_from_directory('/images', filename)
    else:
        return "Image not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)