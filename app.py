import os

from flask import Flask, render_template
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "FlowPilot AI",
        "message": "Backend is running successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)