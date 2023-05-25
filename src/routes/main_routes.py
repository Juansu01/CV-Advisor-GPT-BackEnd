from flask import Blueprint, request

from utils.openai_prompt import get_completion

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return "Home"

@bp.route('/send-message-to-gpt',methods=['POST'])
def about():
    if request.method == 'POST':
        json_data = request.get_json()
        if json_data.get('message'):
            response = get_completion(
                prompt=json_data['message']
            )
            return response

@bp.route('/save-cv',methods=['POST'])
def upload_cv():
    if request.method == 'POST':
        file = request.files['CV']
        file.save(f'src/file_storage{file.filename}')
        return 'File was uploaded.'
