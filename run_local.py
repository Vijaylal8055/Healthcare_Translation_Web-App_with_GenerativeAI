from api.index import app

if __name__ == "__main__":
    print("✅ Using FREE Google Translate API (deep-translator)")
    print("🚀 Running Flask app locally (Vercel-compatible)")
    print("📍 http://127.0.0.1:5000")
    print("📄 Templates loaded from /templates")
    print("\n💡 Press CTRL+C to stop the server\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
    