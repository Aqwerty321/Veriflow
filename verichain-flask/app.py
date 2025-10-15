"""
VeriChain Backend - Flask Application
A proof-of-concept AI-powered product authentication system with blockchain simulation
"""

import os
from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
from io import BytesIO

# Initialize Flask application
app = Flask(__name__)

# Global variable to store the AI model
model = None

def load_ai_model():
    """
    Load the MobileNetV2 model with ImageNet weights.
    This is called once at application startup to avoid reloading on every request.
    """
    global model
    print("Loading MobileNetV2 model... This may take a moment.")
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print("✓ Model loaded successfully!")

def preprocess_image(image):
    """
    Preprocess a PIL Image for the MobileNetV2 model.
    
    Args:
        image: A PIL Image object
        
    Returns:
        A preprocessed numpy array ready for model prediction
    """
    # Resize image to 224x224 pixels (required by MobileNetV2)
    image = image.resize((224, 224))
    
    # Convert PIL Image to numpy array
    img_array = np.array(image)
    
    # Expand dimensions to create a batch of 1: (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess the image using MobileNetV2's preprocessing function
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    return img_array

@app.route('/')
def index():
    """
    Serve the main application page.
    """
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_product():
    """
    API endpoint to analyze an uploaded product image using AI.
    
    Expected: POST request with an image file
    Returns: JSON with product name and confidence score
    """
    try:
        # Validate that a file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read and open the image using Pillow
        image_bytes = file.read()
        image = Image.open(BytesIO(image_bytes))
        
        # Convert to RGB if necessary (handles PNG with alpha channel, etc.)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Preprocess the image for the model
        preprocessed_image = preprocess_image(image)
        
        # Run AI prediction
        predictions = model.predict(preprocessed_image)
        
        # Decode the predictions to get human-readable labels
        # top=1 means we only want the top prediction
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(
            predictions, top=1
        )[0]
        
        # Extract the prediction details
        # decoded_predictions format: [(class_id, label, confidence)]
        class_id, label, confidence = decoded_predictions[0]
        
        # Format the label: replace underscores with spaces and capitalize
        formatted_label = label.replace('_', ' ').title()
        
        # Format confidence as a percentage string
        confidence_percentage = f"{confidence * 100:.1f}%"
        
        # Return the result as JSON
        return jsonify({
            'productName': formatted_label,
            'confidence': confidence_percentage
        })
    
    except Exception as e:
        # Log the error and return a user-friendly message
        print(f"Error during image analysis: {str(e)}")
        return jsonify({
            'error': 'Failed to analyze image. Please try again with a different image.'
        }), 500

# Load the AI model when the application starts
load_ai_model()

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
