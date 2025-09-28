import os
from flask import Flask, render_template

app = Flask(__name__)

GA_MEASUREMENT_ID = os.environ.get("GA_MEASUREMENT_ID")  # will be set on Render

@app.context_processor
def inject_ga():
    return dict(GA_MEASUREMENT_ID=GA_MEASUREMENT_ID)

@app.route('/')
def home():
    # List of moods for the 6 regions
    moods = ["upset", "angry", "nervous", "missing me", "insecure", "broken up"]
    return render_template('index.html', moods=moods)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render gives the port
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
