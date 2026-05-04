import os
from flask import Flask, request
from analyzer import analyze_feedback

app = Flask(__name__)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.route("/analyze", methods=["POST"])
def analyze():
    feedback = request.form.get("feedback", "")

    if not isinstance(feedback, str) or not feedback.strip():
        return {"error": "'feedback' must be a non-empty string"}, 400

    result = analyze_feedback(feedback)
    return result


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5001"))
    app.run(host="0.0.0.0", port=port, debug=False)
