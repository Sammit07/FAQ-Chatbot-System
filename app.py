from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, jsonify
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables first
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

from utils import generate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    if user_input:
        try:
            bot_response = generate_response(user_input)
            return jsonify({"response": bot_response})
        except Exception as e:
            app.logger.error(f"An error occurred: {e}", exc_info=True)  # Log detailed error
            return jsonify({"error": "An error occurred while processing your request."}), 500
    else:
        return jsonify({"error": "Empty message received"}), 400

if __name__ == '__main__':
    app.run(debug=True)


