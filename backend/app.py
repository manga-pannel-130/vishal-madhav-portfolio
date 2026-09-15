# backend/app.py

from pathlib import Path

from flask import Flask, render_template, request, jsonify, abort

from backend.chatbot import get_response
from backend.knowledge import PROJECTS


BASE_DIR = Path(__file__).resolve().parent.parent


app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)


@app.route("/")
def home():
    return render_template(
        "index.html",
        projects=PROJECTS,
    )


@app.route("/project/<project_id>")
def project(project_id):

    project_data = PROJECTS.get(project_id)

    if not project_data:
        abort(404)

    return render_template(
        "project.html",
        project=project_data,
        project_id=project_id,
    )


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:

        return jsonify({
            "response": "Please enter a message."
        }), 400

    user_message = data["message"].strip()

    conversation_history = data.get("history", [])

    bot_response = get_response(
        user_message,
        conversation_history,
    )

    return jsonify({
        "response": bot_response
    })


@app.errorhandler(404)
def not_found(error):
    return render_template("index.html", projects=PROJECTS), 404


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000,
    )