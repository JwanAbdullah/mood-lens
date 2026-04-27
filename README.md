# Mood Lens 😄

A real-time facial expression detection app that turns your webcam into an interactive emotion analyzer.

Built with computer vision and deep learning, Mood Lens detects faces and classifies expressions live — all in your browser or desktop.

---

## 🚀 Features

- Real-time face detection
- Emotion prediction using AI (FER)
- Live webcam feed
- Clean and simple UI (Streamlit optional)

---

## 🧠 Tech Stack

- Python
- OpenCV
- FER (Facial Emotion Recognition)
- TensorFlow
- Streamlit (optional UI)

---

## 📁 Project Structure

```
mood-lens/
│
├── src/
│   ├── main.py        
│   ├── detector.py    
│   └── app.py         
│
├── assets/
│   └── emojis/        
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/mood-lens.git
cd mood-lens
```
2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Run the project

### Option 1: Basic camera test

```bash
python src/main.py
```

### Option 2: Run UI (recommended)

```bash
streamlit run src/app.py
```

---

## 📌 Author

Jwan Abdullah
