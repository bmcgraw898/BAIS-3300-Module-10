# module 10 - Flask Application
# Blaine McGraw 11/3/2025

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # Instead of returning plain text, render your HTML page
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
