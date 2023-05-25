import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

from routes.main_routes import bp

app = Flask(__name__)


if __name__ == "__main__":
    _ = load_dotenv(find_dotenv())
    port = os.getenv('PORT')
    app.register_blueprint(bp)
    app.run(port=port)
