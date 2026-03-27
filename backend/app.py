from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_emergency

app = Flask(__name__)
CORS(app)

def get_solution(emergency):
    solutions = {
        "heart_attack": "Call ambulance immediately. Keep patient calm. Give aspirin if available.",
        "cpr": "Start CPR: Push chest hard and fast (100-120/min).",
        "bleeding": "Apply firm pressure to stop bleeding.",
        "burn": "Cool burn under water for 10 minutes.",
        "fracture": "Immobilize the area. Do not move the person.",
        "poison": "Do not induce vomiting. Call poison control."
    }
    return solutions.get(emergency, "Seek medical help immediately.")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]

    emergency = predict_emergency(text)
    solution = get_solution(emergency)

    return jsonify({
        "type": emergency,
        "solution": solution
    })

if __name__ == "__main__":
    print("Server starting...")
    app.run(debug=True)