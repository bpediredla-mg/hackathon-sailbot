from flask import Blueprint, jsonify, request
from llm_backend import build_qa_chain

api_blueprint = Blueprint('api', __name__)
qa_chain = build_qa_chain()

@api_blueprint.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Flask API!"})

@api_blueprint.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    model = request.json.get("model", "huggingface")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    chain = build_qa_chain(llm_type=model)
    answer = chain.run(question)
    return jsonify({"answer": answer})
