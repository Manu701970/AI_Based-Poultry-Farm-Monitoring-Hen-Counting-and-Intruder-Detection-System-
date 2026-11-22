# 🐔 AI-Based Poultry Farm Monitoring
### Hen Counting and Intruder Detection System Using Computer Vision

An AI-powered poultry farm monitoring system that uses YOLO object detection and tracking to automatically count hens and detect potential intruders from uploaded videos.

## 🚀 Live Demo

**Try the application online:**

👉 https://gpzd2mfzchwmgcnryzknjr.streamlit.app/

No local installation is required to try the online application.

## ✨ Features

- 🐔 **Hen Detection:** Detect hens using a custom-trained YOLO model.
- 🔢 **Hen Counting:** Count unique hens using object tracking IDs.
- 🚨 **Intruder Detection:** Detect potential intruders such as dogs, cats and people.
- 🎥 **Video Processing:** Upload and process videos for poultry farm monitoring.
- 📊 **Monitoring Dashboard:** Display hen counts, intruder counts and processing statistics.
- 📥 **Download Results:** Download processed monitoring results.

## 🛠️ Technologies Used

- Python
- YOLO (Ultralytics)
- OpenCV
- Streamlit
- NumPy
- Pandas

## 🧠 AI Models

- `hen_best.pt` – Custom-trained hen detection model.
- `yolov8n.pt` – YOLO object detection model for intruder detection.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Manu701970/AI_Based-Poultry-Farm-Monitoring-Hen-Counting-and-Intruder-Detection-System-.git
```

### 2. Navigate to the project folder

```bash
cd AI_Based-Poultry-Farm-Monitoring-Hen-Counting-and-Intruder-Detection-System-
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## 📂 Project Structure

```text
├── app.py
├── hen_best.pt
├── yolov8n.pt
├── requirements.txt
├── train_model.py
├── README.md
└── .gitignore
```

## 🎯 Project Objective

The objective of this project is to automate poultry farm monitoring using computer vision, helping farmers monitor hen populations and identify potential intruders through video-based AI detection.

## ⚠️ Disclaimer

Detection and tracking accuracy may vary depending on video quality, lighting, object overlap and tracking conditions.

## 👨‍💻 Project Repository

GitHub: https://github.com/Manu701970/AI_Based-Poultry-Farm-Monitoring-Hen-Counting-and-Intruder-Detection-System-

## 🌐 Live Application

https://gpzd2mfzchwmgcnryzknjr.streamlit.app/

---

**Built with Python, YOLO and Streamlit.**
