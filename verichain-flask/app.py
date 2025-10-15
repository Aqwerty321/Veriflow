"""
VeriChain Backend - Flask Application
A proof-of-concept AI-powered product authentication system with blockchain simulation
"""

import os
import hashlib
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
from io import BytesIO

# Initialize Flask application
app = Flask(__name__)

# Configure maximum file upload size (10MB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Global variable to store the AI model
model = None

# In-memory storage for recent certifications (for demo purposes)
certification_history = []

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
        
        # Generate a unique product ID based on image hash
        image_hash = hashlib.sha256(image_bytes).hexdigest()[:16]
        product_id = f"VRC-{image_hash.upper()}"
        
        # Return the result as JSON
        return jsonify({
            'productName': formatted_label,
            'confidence': confidence_percentage,
            'productId': product_id,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        # Log the error and return a user-friendly message
        print(f"Error during image analysis: {str(e)}")
        return jsonify({
            'error': 'Failed to analyze image. Please try again with a different image.'
        }), 500

@app.route('/certify', methods=['POST'])
def certify_product():
    """
    API endpoint to simulate blockchain certification.
    
    Expected: POST request with product details
    Returns: JSON with blockchain transaction details
    """
    try:
        data = request.json
        
        # Generate a realistic transaction hash
        tx_data = f"{data.get('productId')}{data.get('productName')}{time.time()}"
        tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
        
        # Create certification record
        certification = {
            'productId': data.get('productId'),
            'productName': data.get('productName'),
            'confidence': data.get('confidence'),
            'txHash': f"0x{tx_hash}",
            'blockNumber': len(certification_history) + 1000000,  # Simulated block number
            'timestamp': datetime.now().isoformat(),
            'status': 'confirmed'
        }
        
        # Store in history (keep last 50)
        certification_history.append(certification)
        if len(certification_history) > 50:
            certification_history.pop(0)
        
        return jsonify(certification)
    
    except Exception as e:
        print(f"Error during certification: {str(e)}")
        return jsonify({
            'error': 'Failed to certify product. Please try again.'
        }), 500

@app.route('/history', methods=['GET'])
def get_history():
    """
    API endpoint to retrieve recent certification history.
    
    Returns: JSON array of recent certifications
    """
    # Return the last 10 certifications in reverse order (newest first)
    return jsonify(certification_history[-10:][::-1])

@app.route('/health', methods=['GET'])
def health_check():
    """
    API endpoint for health checking.
    
    Returns: JSON with server status
    """
    return jsonify({
        'status': 'healthy',
        'modelLoaded': model is not None,
        'timestamp': datetime.now().isoformat(),
        'totalCertifications': len(certification_history)
    })

# Load the AI model when the application starts
load_ai_model()

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
