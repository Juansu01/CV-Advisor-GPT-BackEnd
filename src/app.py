import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS

from routes.main_routes import bp

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = '/src/file_storage'


if __name__ == "__main__":
    _ = load_dotenv(find_dotenv())
    port = os.getenv('PORT')
    app.register_blueprint(bp)
    app.run(port=port)
