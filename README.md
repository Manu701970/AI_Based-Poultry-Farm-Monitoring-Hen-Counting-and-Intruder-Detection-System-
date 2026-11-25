🐔 AI-Based Poultry Farm Monitoring System

Smart Hen Counting and Intruder Detection Using Computer Vision

An AI-powered poultry farm monitoring application that uses computer vision and YOLO object detection to identify and count hens and detect potential intruders from images or video streams.

<p align="center">
  <a href="https://gpzd2mfzchwmgcnryzknjr.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Live Demo">
  </a>
  <a href="https://github.com/Manu701970/AI_Based-Poultry-Farm-Monitoring-Hen-Counting-and-Intruder-Detection-System-">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>---

🚀 Live Application

Try the project here:

👉 https://gpzd2mfzchwmgcnryzknjr.streamlit.app/

📌 Project Overview

Traditional poultry farm monitoring often requires continuous manual observation. This project aims to simplify monitoring through AI-based computer vision.

The system processes visual input and detects objects using a trained YOLO model. It provides an interface for monitoring hen counts and identifying potential intruders.

✨ Key Features

- 🐔 Hen Detection: Identifies hens using YOLO object detection.
- 🔢 Automatic Hen Counting: Counts detected hens in the input.
- 🚨 Intruder Detection: Identifies objects classified as potential intruders by the trained model.
- 🎥 Visual Monitoring: Supports the project's image/video monitoring workflow.
- 📊 Interactive Dashboard: Displays detection results through Streamlit.
- ⚡ AI-Based Processing: Uses computer vision for automated detection.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming
YOLOv8 / Ultralytics| Object detection
OpenCV| Image and video processing
Streamlit| Web application
NumPy| Numerical operations
Pandas| Data handling

🏗️ System Workflow

1. Upload or provide visual input.
2. The application processes the input.
3. The trained YOLO model detects objects.
4. Detected hens are counted.
5. Potential intruders are identified based on model classes.
6. Results are displayed in the dashboard.

📂 Project Structure

AI-Poultry-Farm-Monitoring/
│
├── app.py
├── train_model.py
├── hen_best.pt
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
│
└── Other project files

The structure above is illustrative; actual files may vary.

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/Manu701970/AI_Based-Poultry-Farm-Monitoring-Hen-Counting-and-Intruder-Detection-System-.git

2. Open the project folder

cd AI_Based-Poultry-Farm-Monitoring-Hen-Counting-and-Intruder-Detection-System-

3. Create a virtual environment

python -m venv venv

4. Activate the environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the application

streamlit run app.py

The application will open in your browser.

🧠 Model Information

The project uses the Ultralytics YOLO framework for object detection.

The trained model file is:

hen_best.pt

The model's detection performance depends on the quality of the training dataset and input images or videos.

☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Live link: https://gpzd2mfzchwmgcnryzknjr.streamlit.app/

🔮 Future Enhancements

- Real-time CCTV camera integration.
- Improved intruder classification.
- Poultry activity monitoring.
- Historical detection reports.
- Email or mobile alerts.
- Database integration for monitoring records.

🎯 Applications

- Poultry farms
- Smart agriculture
- Livestock monitoring
- Automated farm security
- AI-based animal detection research

👨‍💻 Author

Manu S MANU

GitHub: https://github.com/Manu701970

⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

---

Developed using Python, YOLO, OpenCV and Streamlit.