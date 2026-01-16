from flask import Flask, jsonify, request
import os
import cv2
import numpy as np
import random

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
# Disease Class Mapping (Day 6)
# -----------------------------
DISEASE_CLASSES = {
    0: "Healthy",
    1: "Leaf Blight",
    2: "Leaf Spot",
    3: "Powdery Mildew",
    4: "Rust"
}

# -----------------------------
# Model Inference Placeholder
# -----------------------------
def load_model_and_predict(processed_image):
    """
    Placeholder for real AI model inference
    """
    predicted_class = random.randint(0, len(DISEASE_CLASSES) - 1)
    confidence = round(random.uniform(0.75, 0.95), 2)
    return predicted_class, confidence

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

    # Image preprocessing
    processed_image = preprocess_image(image_path)

    # Model inference (Day 6 placeholder)
    predicted_class, confidence = load_model_and_predict(processed_image)
    disease_name = DISEASE_CLASSES[predicted_class]

    prediction = {
        "disease": disease_name,
        "confidence": confidence,
        "advice": "Use recommended fungicide and monitor crop regularly"
    }

    return jsonify({
        "message": "Image processed and disease predicted successfully",
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)