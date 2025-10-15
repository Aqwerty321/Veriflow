# VeriChain - AI-Powered Product Authentication System

A proof-of-concept web application that uses AI for product identification and simulates blockchain-based certificate issuance.

## 🚀 Features

- **AI Product Recognition**: Uses MobileNetV2 (pre-trained on ImageNet) to identify products from images
- **Confidence Scoring**: Provides confidence scores for product identification
- **Blockchain Simulation**: Simulates certificate minting on a blockchain
- **Modern UI**: Dark-themed, responsive interface built with Tailwind CSS
- **Real-time Analysis**: Instant product identification with visual feedback

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd verichain-flask
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. **Upload a product image** (shoes, watches, coffee mugs, etc.)

4. **Click "Analyze Product"** to run AI identification

5. **Click "Certify on Blockchain"** to simulate certificate issuance

## 📁 Project Structure

```
verichain-flask/
├── app.py              # Flask backend with AI logic and API endpoints
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend UI (HTML, CSS, JavaScript)
├── static/            # Static assets (CSS, JS, images)
└── README.md          # This file
```

## 🧠 How It Works

1. **Image Upload**: User uploads a product image through the web interface
2. **Preprocessing**: Image is resized to 224x224 and preprocessed for MobileNetV2
3. **AI Analysis**: MobileNetV2 model classifies the product
4. **Results Display**: Top prediction with confidence score is shown
5. **Blockchain Simulation**: User can simulate certificate minting with a mock transaction hash

## 🔧 Technology Stack

- **Backend**: Python 3, Flask
- **AI/ML**: TensorFlow (Keras), MobileNetV2
- **Image Processing**: Pillow, NumPy
- **Frontend**: HTML5, Tailwind CSS, JavaScript (Fetch API)

## ⚠️ Notes

- This is a **proof-of-concept** for demonstration purposes
- The blockchain functionality is **simulated** (no actual blockchain integration)
- The AI model uses ImageNet classes, so it works best with common objects
- For production use, consider:
  - Custom model training for specific product categories
  - Actual blockchain integration (e.g., Ethereum, Polygon)
  - User authentication and database storage
  - Production WSGI server (e.g., Gunicorn)

## 📝 License

This project is created for educational and hackathon purposes.

## 🤝 Contributing

This is a hackathon project, but feel free to fork and enhance it!

## 📧 Contact

For questions or feedback, please contact the project maintainer.
