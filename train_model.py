
from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="chicken.yaml",
        epochs=15,
        imgsz=416,
        batch=2,
        workers=0,
        patience=5,
        device="cpu",
        project="runs",
        name="hen_detection_fast",
        exist_ok=True
    )

if __name__ == "__main__":
    main()
