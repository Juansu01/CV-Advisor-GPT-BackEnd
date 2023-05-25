from flask import Blueprint
from utils.openai_prompt import get_completion

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return get_completion()

@bp.route('/about')
def about():
    return 'About page'

