# from flask import Flask, request, jsonify
# from flask_cors import CORS

# from nlp.task_classifier import classify_task
# from agent.tool_selector import select_tool
# from agent.executor import execute_tool
# from response.formatter import format_response

# app = Flask(__name__)
# CORS(app)

# @app.route("/", methods=["GET"])
# def health_check():
#     return {
#         "status": "running",
#         "message": "Agentic AI backend is live 🚀"
#     }

# chat_history = []

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.json
#     user_msg = data["message"]

#     task = classify_task(user_msg)
#     tool = select_tool(task)
#     result = execute_tool(tool, user_msg)

#     bot_msg = f"🧠 Task: {task}\n🔧 Tool: {tool}\n📌 Result: {result}"

#     chat_history.append({
#         "user": user_msg,
#         "bot": bot_msg
#     })

#     return jsonify({
#         "reply": bot_msg,
#         "history": chat_history[-5:]  # last 5 turns
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from nlp.task_classifier import classify_task
from agent.tool_selector import select_tool
from agent.executor import execute_tool

app = Flask(__name__)
CORS(app)

FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

@app.route("/")
def serve_frontend():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "message": "Agentic AI backend is live 🚀"
    })

chat_history = []

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "")

    task = classify_task(user_msg)
    tool = select_tool(task)
    result = execute_tool(tool, user_msg)

    bot_msg = f"🧠 Task: {task}\n🔧 Tool: {tool}\n📌 Result: {result}"

    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
