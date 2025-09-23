from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # List of moods for the 6 regions
    moods = ["upset", "angry", "nervous", "missing me", "insecure", "alone"]
    return render_template('index.html', moods=moods)

if __name__ == '__main__':
    app.run(debug=True)
