from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator
import os
import hashlib

app = Flask(__name__, template_folder='../templates')

CORS(app, resources={r"/*": {"origins": ["*"], "methods": ["GET", "POST"]}})

request_counts = {}

def check_rate_limit(ip):
    import time
    current_time = time.time()
    if ip not in request_counts:
        request_counts[ip] = []
    request_counts[ip] = [t for t in request_counts[ip] if current_time - t < 60]
    if len(request_counts[ip]) >= 30:
        return False
    request_counts[ip].append(current_time)
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        client_ip = request.remote_addr
        if not check_rate_limit(client_ip):
            return jsonify({'error': 'Rate limit exceeded'}), 429
        
        data = request.json
        text = data.get('text', '')
        source_lang = data.get('source_lang', 'en')
        target_lang = data.get('target_lang', 'es')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        if len(text) > 5000:
            return jsonify({'error': 'Text too long'}), 400
        
        text = text.replace('<', '&lt;').replace('>', '&gt;')
        
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translation = translator.translate(text)
        
        return jsonify({
            'success': True,
            'translation': translation,
            'original': text
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Translation failed'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200
