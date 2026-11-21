writing{variant="document" id="83419"}
# AI-Based Poultry Farm Monitoring, Hen Counting and Intruder Detection System Using Computer Vision

## Project Overview

This project is an AI-based poultry farm monitoring system developed using computer vision and deep learning. It uses YOLO (You Only Look Once), OpenCV and Streamlit to detect, track and monitor chickens in video footage.

The system also identifies potential intruders such as dogs, cats and people using object detection.

## Features

- AI-based chicken detection using a custom-trained YOLO model.
- Chicken detection and tracking using tracking IDs.
- Video-based poultry monitoring.
- Intruder detection for people, dogs and cats.
- Bounding-box visualization.
- Poultry monitoring analytics.
- Processed video preview and download.
- Streamlit web-based dashboard.

## Technologies Used

- Python
- YOLOv8
- OpenCV
- Streamlit
- ByteTrack
- Roboflow

## Project Structure

```text
Smart-Poultry-Farm-Monitoring/
├── app.py
├── train_model.py
├── chicken.yaml
├── requirements.txt
├── poultry-chicken-1/
└── README.md
```

## Project Workflow

1. Dataset collection using Roboflow.
2. Dataset preprocessing and label conversion.
3. Custom YOLO model training.
4. Chicken detection and tracking.
5. Intruder detection using a pretrained YOLO model.
6. Video analytics and visualization using Streamlit.

## Objective

The main objective is to automate poultry farm monitoring, improve chicken counting and provide visual detection of potential intruders through computer vision.

## Disclaimer

Chicken counts and tracking results depend on video quality, camera angle, lighting, occlusion and model accuracy. Intruder detection is intended as a visual monitoring aid.

:::