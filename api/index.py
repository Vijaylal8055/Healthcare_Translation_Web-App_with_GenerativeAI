from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import openai
import os
from dotenv import load_dotenv
import hashlib
import secrets

load_dotenv()

app = Flask(__name__, template_folder="../templates")

# -------------------- SECURITY --------------------

CORS(app, resources={
    r"/*": {
        "origins": ["https://*.vercel.app"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})

if os.getenv("VERCEL_ENV") == "production":
    Talisman(
        app,
        force_https=True,
        strict_transport_security=True,
        content_security_policy={
            "default-src": "'self'",
            "script-src": ["'self'", "'unsafe-inline'", "https://cdn.tailwindcss.com"],
            "style-src": ["'self'", "'unsafe-inline'"],
            "img-src": "'self' data:",
        },
    )

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)
limiter.init_app(app)

app.secret_key = os.getenv("SECRET_KEY", secrets.token_hex(32))
openai.api_key = os.getenv("OPENAI_API_KEY")

# -------------------- ROUTES --------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
@limiter.limit("30 per minute")
def translate():
    try:
        data = request.json
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        if len(text) > 5000:
            return jsonify({"error": "Text too long"}), 400

        text = text.replace("<", "&lt;").replace(">", "&gt;")

        lang_names = {
            "en": "English", "es": "Spanish", "zh": "Chinese",
            "fr": "French", "ar": "Arabic", "hi": "Hindi",
            "pt": "Portuguese", "ru": "Russian", "ja": "Japanese",
            "de": "German"
        }

        source = lang_names.get(data.get("source_lang", "en"), "English")
        target = lang_names.get(data.get("target_lang", "es"), "Spanish")

        req_hash = hashlib.sha256(text.encode()).hexdigest()[:10]
        print(f"Translate {source} → {target} | {req_hash}")

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional medical translator. "
                        "Preserve medical terminology and privacy."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Translate from {source} to {target}:\n\n{text}",
                },
            ],
            temperature=0.3,
            max_tokens=500,
        )

        return jsonify({
            "success": True,
            "translation": response.choices[0].message["content"].strip()
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": "Translation service unavailable"}), 500

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Rate limit exceeded"}), 429
