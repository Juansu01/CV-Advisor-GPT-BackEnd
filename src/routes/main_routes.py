from flask import Blueprint, request, jsonify
from openai.error import RateLimitError

from utils.openai_prompt import get_completion, initialize_cv_context
from utils.read_pdf import read_pdf

bp = Blueprint('routes', __name__)

MESSAGES = []

@bp.route('/')
def home():
    return "Home"

@bp.route('/send-message-to-gpt',methods=['POST'])
def gpt_message():
    print("HELLOOO!")
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        if json_data.get('message'):
            global MESSAGES
            try:
                response, new_messages = get_completion(
                    messages=MESSAGES,
                    prompt=json_data['message']
            )
                MESSAGES = new_messages
            except RateLimitError:
                return "The model we're using is overloaded, please try again later."
            return jsonify({'response': response})

@bp.route('/save-cv',methods=['POST'])
def upload_cv():
    if request.method == 'POST':
        file = request.files['file']
        file.save(f'src/file_storage/{file.filename}')
        return 'File was uploaded.', 200

@bp.route('/initialize-context/<cv_name>',methods=['POST'])
def initialize_context(cv_name):
    if request.method == 'POST':
        print(f"REQUESTING INITIALIZATION FOR: {cv_name}")
        text = read_pdf(f'src/file_storage/{cv_name}')
        global MESSAGES
        MESSAGES = initialize_cv_context(text)
        try:
            response, new_messages = get_completion(
                messages=MESSAGES,
                prompt="""Say hello using the name in my CV,
                tell me what you can do for me."""
            )
            MESSAGES = new_messages
        except RateLimitError:
                return "The model we're using is overloaded, please try again later.", 500
        return jsonify({'response': response})
