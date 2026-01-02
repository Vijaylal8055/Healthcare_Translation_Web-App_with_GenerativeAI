# 🏥 Healthcare Translation Web App with Generative AI

A real-time medical translation web application powered by AI, designed for healthcare providers and patients to communicate across language barriers.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎤 **Real-time Speech Recognition** - Speak naturally and get instant translations
- 🌍 **10+ Languages Supported** - English, Spanish, Chinese, French, Arabic, Hindi, Portuguese, Russian, Japanese, German
- 🔄 **Bidirectional Translation** - Switch between patient and provider modes
- 🔊 **Text-to-Speech Output** - Hear translations spoken aloud
- 🔒 **Privacy-First Design** - No data stored permanently, HIPAA-conscious
- ⚡ **Fast & Free** - Uses Google Translate API (no API key required)
- 🎨 **Modern UI** - Clean, responsive interface built with Tailwind CSS

## 🚀 Demo

**Live Demo:** [Deploy on Vercel](https://vercel.com)

**Screenshot:**
```
┌─────────────────────────────────────────┐
│  Healthcare Translation Web App         │
├─────────────────────────────────────────┤
│  Speaking: English  →  Spanish          │
│                                         │
│  [🎤 Tap to Start]                      │
│                                         │
│  Original         │   Translation       │
│  "I have pain..." │  "Tengo dolor..."   │
└─────────────────────────────────────────┘
```

## 📋 Prerequisites

- Python 3.8 or higher
- Web browser with speech recognition support (Chrome, Edge)
- Internet connection (for translation API)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-translation-app.git
cd healthcare-translation-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- Flask 3.0.0
- flask-cors 4.0.0
- deep-translator 1.11.4
- Werkzeug 3.0.1

### 3. Run Locally

```bash
python run_local.py
```

The app will be available at `http://127.0.0.1:5000`

## 📁 Project Structure

```
NaoMedical/
├── api/
│   └── index.py          # Main Flask application
├── templates/
│   └── index.html        # Frontend interface
├── run_local.py          # Local development server
├── vercel.json           # Vercel deployment config
├── requirements.txt      # Python dependencies
├── .vercelignore         # Vercel ignore file
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🌐 Deployment

### Deploy to Vercel (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel
   ```

4. **Production Deployment:**
   ```bash
   vercel --prod
   ```

Your app will be live at `https://your-app.vercel.app`

### Deploy to Other Platforms

**Render.com:**
- Connect your GitHub repository
- Select "Python" environment
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn api.index:app`

**Railway.app:**
- Connect repository
- Railway auto-detects Python and deploys

## 🔒 Security Features

- ✅ Rate limiting (30 requests/minute)
- ✅ Input validation & sanitization
- ✅ XSS prevention
- ✅ CORS protection
- ✅ No data persistence (privacy-first)
- ✅ Request logging (anonymized with hashing)

## 🎯 Usage

### Basic Workflow

1. **Select Languages**
   - Choose your speaking language (input)
   - Choose the translation language (output)

2. **Start Recording**
   - Click the microphone button
   - Speak clearly in your selected language
   - Watch real-time transcription appear

3. **View Translation**
   - Translation appears automatically
   - Click "Speak Translation" to hear it aloud

4. **Switch Modes**
   - Click "Patient/Provider" button to swap languages
   - Perfect for two-way conversations

### Supported Languages

| Code | Language   | Native Name |
|------|-----------|-------------|
| en   | English   | English     |
| es   | Spanish   | Español     |
| zh   | Chinese   | 中文        |
| fr   | French    | Français    |
| ar   | Arabic    | العربية     |
| hi   | Hindi     | हिन्दी      |
| pt   | Portuguese| Português   |
| ru   | Russian   | Русский     |
| ja   | Japanese  | 日本語      |
| de   | German    | Deutsch     |

## 🔧 Configuration

### Rate Limiting

Adjust in `api/index.py`:
```python
if len(request_counts[ip]) >= 30:  # Change limit here
    return False
```

### Text Length Limit

Modify in `api/index.py`:
```python
if len(text) > 5000:  # Change max characters
    return jsonify({'error': 'Text too long'}), 400
```

## 🧪 Testing

### Health Check Endpoint

```bash
curl http://localhost:5000/health
```

Response:
```json
{"status": "healthy", "service": "Healthcare Translation API"}
```

### Manual Translation Test

```bash
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello","source_lang":"en","target_lang":"es"}'
```

## 🐛 Troubleshooting

### Speech Recognition Not Working
- **Issue:** Microphone not detected
- **Solution:** Use Chrome or Edge browser, grant microphone permissions

### Translation Fails
- **Issue:** "Translation service temporarily unavailable"
- **Solution:** Check internet connection, Google Translate may be rate-limited

### ModuleNotFoundError
- **Issue:** `No module named 'deep_translator'`
- **Solution:** Run `pip install -r requirements.txt`

### Port Already in Use
- **Issue:** `Address already in use`
- **Solution:** Change port in `run_local.py`:
  ```python
  app.run(host="127.0.0.1", port=5001, debug=True)
  ```

## 📊 API Endpoints

### `GET /`
Returns the main HTML interface

### `POST /translate`
Translates text from one language to another

**Request Body:**
```json
{
  "text": "Hello, how are you?",
  "source_lang": "en",
  "target_lang": "es"
}
```

**Response:**
```json
{
  "success": true,
  "translation": "Hola, ¿cómo estás?",
  "original": "Hello, how are you?"
}
```

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "service": "Healthcare Translation API"
}
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Translate API** - Free translation service
- **deep-translator** - Python translation library
- **Flask** - Web framework
- **Tailwind CSS** - UI styling

## 📧 Contact

**Project Maintainer:** Vijay Lal

**Issues:** [GitHub Issues](https://github.com/yourusername/healthcare-translation-app/issues)

## 🔮 Future Enhancements

- [ ] Add medical terminology database
- [ ] Support for more languages
- [ ] Offline mode with cached translations
- [ ] Mobile app version
- [ ] Voice authentication for security
- [ ] Integration with EHR systems
- [ ] Multi-user conversation support
- [ ] Export conversation transcripts

## ⚠️ Disclaimer

This application is intended as a communication aid and should not replace professional medical interpretation services for critical medical decisions. Always use certified medical interpreters for important healthcare communications.

---

Made with ❤️ for healthcare workers and patients worldwide# Healthcare_Translation_Web-App_with_GenerativeAI