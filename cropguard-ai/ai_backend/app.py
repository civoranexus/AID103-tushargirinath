from flask import Flask, jsonify, request
import os
import cv2
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Image Preprocessing Function
# -----------------------------
def preprocess_image(image_path):
    """
    Preprocess image for AI model input
    """
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0          # normalize
    image = np.expand_dims(image, axis=0)
    return image

# -----------------------------
# Routes
# -----------------------------
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

    # ✅ Image preprocessing (Day 5 work)
    processed_image = preprocess_image(image_path)

    # Dummy AI prediction (placeholder)
    prediction = {
        "disease": "Leaf Blight",
        "confidence": "0.87",
        "advice": "Use recommended fungicide and monitor crop regularly"
    }

    return jsonify({
        "message": "Image received and preprocessed successfully",
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
