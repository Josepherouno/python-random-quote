import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.')
client = OpenAI()

@app.get('/')
def index():
    return send_from_directory('.', 'index.html')

@app.post('/chat')
def chat():
    data = request.get_json(force=True)
    message = data.get('message', '')
    if not message:
        return jsonify({'response': 'I did not hear anything.'}), 400
    completion = client.responses.create(
        model='gpt-4o-mini',
        input=message,
    )
    reply = completion.output_text
    return jsonify({'response': reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
