from flask import Flask, jsonify, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "CropGuard AI",
        "status": "Backend running successfully"
    })

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "OK",
        "message": "CropGuard AI API is healthy"
    })

@app.route("/predict", methods=["POST"])
def predict_disease():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Dummy AI prediction (placeholder)
    prediction = {
        "disease": "Leaf Blight",
        "confidence": "0.87",
        "advice": "Use recommended fungicide and monitor crop regularly"
    }

    return jsonify({
        "message": "Image received successfully",
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)