# app.py

from flask import Flask, render_template, request, jsonify

from chatbot import get_response


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:

        return jsonify({
            "response": "Please enter a message."
        }), 400

    user_message = data["message"]

    bot_response = get_response(user_message)

    return jsonify({
        "response": bot_response
    })


if __name__ == "__main__":
    app.run(debug=True)