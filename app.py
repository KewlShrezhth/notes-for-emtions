from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # List of moods for the 6 regions
    moods = ["upset", "angry", "nervous", "missing me", "insecure", "broken up"]
    return render_template('index.html', moods=moods)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render gives you a port
    app.run(host="0.0.0.0", port=port)
