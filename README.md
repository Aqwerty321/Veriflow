# VeriChain - AI-Powered Product Authentication System

<div align="center">
  
  🔐 **Blockchain-Verified Product Authentication Using AI**
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
  [![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://www.tensorflow.org/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 🌟 Overview

VeriChain is a proof-of-concept web application that combines **artificial intelligence** with **blockchain technology** to authenticate products and issue digital certificates. Built for hackathons and demonstrations, it showcases the power of modern ML models in product verification workflows.

### ✨ Key Features

- 🤖 **AI Product Recognition** - Powered by MobileNetV2 trained on ImageNet
- 📊 **Confidence Scoring** - Real-time accuracy metrics for identification
- ⛓️ **Blockchain Simulation** - Mock certificate minting with transaction tracking
- 📜 **Certification History** - Track and view past product verifications
- 💾 **Certificate Download** - Export verification data as JSON
- 🎨 **Modern UI** - Dark-themed, responsive design with Tailwind CSS
- 🔔 **Toast Notifications** - Real-time feedback for user actions
- 📤 **Share Functionality** - Easy certificate sharing

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aqwerty321/Veriflow.git
   cd Veriflow/verichain-flask
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Demo

1. Upload an image of any product (shoe, watch, coffee mug, etc.)
2. Click **"Analyze Product"** to run AI identification
3. View the product name, confidence score, and unique ID
4. Click **"Certify on Blockchain"** to issue a digital certificate
5. Download or share your certificate

---

## 🏗️ Project Structure

```
Veriflow/
├── verichain-flask/
│   ├── app.py              # Flask backend with AI logic
│   ├── requirements.txt    # Python dependencies
│   ├── templates/
│   │   └── index.html      # Frontend UI
│   ├── static/             # Static assets
│   └── .gitignore          # Git ignore rules
└── README.md               # This file
```

---

## 🧠 How It Works

```mermaid
graph LR
    A[Upload Image] --> B[Preprocess]
    B --> C[MobileNetV2 AI]
    C --> D[Product Identified]
    D --> E[Generate Product ID]
    E --> F[User Certifies]
    F --> G[Blockchain Simulation]
    G --> H[Certificate Issued]
```

1. **Image Upload** - User uploads product image via web interface
2. **Preprocessing** - Image resized to 224x224 and normalized
3. **AI Classification** - MobileNetV2 identifies the product
4. **Product ID Generation** - Unique hash-based identifier created
5. **Certification** - Simulated blockchain transaction with TX hash
6. **History Tracking** - Certificate stored in session history

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3, Flask |
| **AI/ML** | TensorFlow 2.x, Keras, MobileNetV2 |
| **Image Processing** | Pillow, NumPy |
| **Frontend** | HTML5, Tailwind CSS, JavaScript ES6+ |
| **APIs** | RESTful endpoints with JSON |

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve main application page |
| `/analyze` | POST | Analyze product image with AI |
| `/certify` | POST | Issue blockchain certificate |
| `/history` | GET | Retrieve certification history |
| `/health` | GET | Health check and status |

---

## 🎯 Use Cases

- **Product Authentication** - Verify genuine products vs counterfeits
- **Supply Chain Tracking** - Document product provenance
- **Quality Assurance** - Automated product identification
- **E-commerce** - Enhanced product listings with AI verification
- **Inventory Management** - Smart cataloging systems

---

## ⚠️ Important Notes

- **Proof of Concept** - This is a demonstration project for hackathons
- **Simulated Blockchain** - No actual blockchain integration (yet!)
- **ImageNet Classes** - Works best with common objects in the training set
- **Not Production-Ready** - Requires enhancements for production use

### For Production Deployment:

- [ ] Train custom model for specific product categories
- [ ] Integrate real blockchain (Ethereum, Polygon, etc.)
- [ ] Add user authentication and authorization
- [ ] Implement database for persistent storage
- [ ] Use production WSGI server (Gunicorn/uWSGI)
- [ ] Add rate limiting and security measures
- [ ] Implement comprehensive error handling
- [ ] Add monitoring and logging

---

## 🤝 Contributing

This is a hackathon project, but contributions are welcome! Feel free to:

- Fork the repository
- Create a feature branch
- Submit a pull request

---

## 📝 License

This project is open source and available for educational purposes.

---

## 👨‍💻 Author

**Aqwerty321**

- GitHub: [@Aqwerty321](https://github.com/Aqwerty321)

---

## 🙏 Acknowledgments

- TensorFlow team for MobileNetV2
- Flask community for excellent documentation
- Tailwind CSS for beautiful styling utilities

---

<div align="center">
  
  **Made with ❤️ for the hackathon community**
  
  ⭐ Star this repo if you find it helpful!
  
</div>
