from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return 'Welcome to the home page'

@bp.route('/about')
def about():
    return 'About page'

