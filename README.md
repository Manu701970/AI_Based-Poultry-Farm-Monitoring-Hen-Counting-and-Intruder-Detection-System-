# AI-Based Poultry Farm Monitoring, Hen Counting and Intruder Detection System

An AI-powered poultry farm monitoring system using computer vision and YOLO to detect and count hens and identify potential intruders.

## Features
- AI-based hen detection and counting
- Intruder detection using YOLO
- Video upload and processing
- Real-time detection visualization
- Streamlit web dashboard

## Technologies Used
- Python
- Streamlit
- OpenCV
- Ultralytics YOLO

## Models
- `hen_best.pt` – Custom-trained hen detection model
- `yolov8n.pt` – Intruder/object detection model

## How to Run Locally

1. Clone this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Project Purpose

This project aims to improve poultry farm monitoring through computer vision by automating hen counting and detecting potential intruders.

---

Developed as an AI-based computer vision project.