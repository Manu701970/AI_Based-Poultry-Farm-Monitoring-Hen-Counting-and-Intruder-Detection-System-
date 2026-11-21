
import streamlit as st
import cv2
import tempfile
import os
import time
from collections import Counter
from ultralytics import YOLO

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Poultry Farm Monitoring",
    page_icon="🐔",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🐔 AI-Based Poultry Farm Monitoring")
st.subheader("Hen Counting and Intruder Detection System")
st.write(
    "Automated poultry farm monitoring using custom YOLO detection "
    "and tracking with computer vision."
)

# ---------------- MODEL PATH ----------------
HEN_MODEL_PATH = "hen_best.pt"
INTRUDER_MODEL_PATH = "yolov8n.pt"

# ---------------- LOAD MODELS ----------------
@st.cache_resource
def load_models():
    hen_model = YOLO(HEN_MODEL_PATH)
    intruder_model = YOLO(INTRUDER_MODEL_PATH)
    return hen_model, intruder_model

if not os.path.exists(HEN_MODEL_PATH):
    st.error("hen_best.pt not found in the project directory.")
    st.stop()

if not os.path.exists(INTRUDER_MODEL_PATH):
    st.error("yolov8n.pt not found in the project directory.")
    st.stop()

try:
    hen_model, intruder_model = load_models()
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.header("Detection Settings")

hen_conf = st.sidebar.slider(
    "Hen confidence",
    min_value=0.10,
    max_value=0.90,
    value=0.35,
    step=0.05
)

intruder_conf = st.sidebar.slider(
    "Intruder confidence",
    min_value=0.30,
    max_value=0.90,
    value=0.55,
    step=0.05
)

# ---------------- UPLOAD VIDEO ----------------
uploaded_file = st.file_uploader(
    "Upload poultry farm video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file is not None:

    st.video(uploaded_file)

    if st.button("🚀 Start Monitoring", type="primary"):

        # ---------------- TEMP INPUT ----------------
        input_temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )

        input_temp.write(uploaded_file.getbuffer())
        input_temp.close()

        input_video = input_temp.name

        cap = cv2.VideoCapture(input_video)

        if not cap.isOpened():
            st.error("Could not open the uploaded video.")
            st.stop()

        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps <= 0:
            fps = 25

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # ---------------- TEMP OUTPUT ----------------
        output_temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )
        output_temp.close()

        output_video = output_temp.name

        writer = cv2.VideoWriter(
            output_video,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height)
        )

        # ---------------- DISPLAY ----------------
        video_placeholder = st.empty()
        progress_bar = st.progress(0)
        status_text = st.empty()

        # ---------------- TRACKING SETS ----------------
        unique_hen_ids = set()
        unique_intruder_ids = set()

        intruder_class_counts = Counter()

        frame_number = 0
        start_time = time.time()

        # COCO classes:
        # 0 = person, 15 = cat, 16 = dog
        intruder_classes = [0, 15, 16]

        try:

            while True:

                ret, frame = cap.read()

                if not ret:
                    break

                frame_number += 1

                # ---------------- HEN TRACKING ----------------
                hen_results = hen_model.track(
                    source=frame,
                    persist=True,
                    tracker="bytetrack.yaml",
                    conf=hen_conf,
                    imgsz=416,
                    verbose=False
                )

                hen_result = hen_results[0]

                # Draw hen boxes and IDs
                annotated_frame = hen_result.plot()

                current_hens = 0

                if hen_result.boxes is not None:

                    hen_boxes = hen_result.boxes

                    if hen_boxes.id is not None:

                        hen_ids = hen_boxes.id.int().cpu().tolist()

                        current_hens = len(hen_ids)

                        for track_id in hen_ids:
                            unique_hen_ids.add(int(track_id))

                # ---------------- INTRUDER TRACKING ----------------
                intruder_results = intruder_model.track(
                    source=frame,
                    persist=True,
                    tracker="bytetrack.yaml",
                    classes=intruder_classes,
                    conf=intruder_conf,
                    imgsz=416,
                    verbose=False
                )

                intruder_result = intruder_results[0]

                current_intruders = 0

                if intruder_result.boxes is not None:

                    boxes = intruder_result.boxes

                    if boxes.id is not None:

                        ids = boxes.id.int().cpu().tolist()
                        class_ids = boxes.cls.int().cpu().tolist()
                        confidences = boxes.conf.cpu().tolist()
                        coordinates = boxes.xyxy.int().cpu().tolist()

                        current_intruders = len(ids)

                        for track_id, cls_id, confidence, xyxy in zip(
                            ids, class_ids, confidences, coordinates
                        ):

                            class_name = intruder_model.names[int(cls_id)]

                            # Unique combination of class and ID
                            key = (class_name, int(track_id))
                            unique_intruder_ids.add(key)

                            x1, y1, x2, y2 = xyxy

                            # Draw intruder box
                            cv2.rectangle(
                                annotated_frame,
                                (x1, y1),
                                (x2, y2),
                                (0, 0, 255),
                                2
                            )

                            label = (
                                f"INTRUDER {class_name} "
                                f"ID:{track_id} {confidence:.2f}"
                            )

                            cv2.putText(
                                annotated_frame,
                                label,
                                (x1, max(y1 - 10, 20)),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.55,
                                (0, 0, 255),
                                2
                            )

                # ---------------- OVERLAY ----------------
                cv2.putText(
                    annotated_frame,
                    f"Hens Visible: {current_hens}",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    annotated_frame,
                    f"Unique Hens: {len(unique_hen_ids)}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )

                cv2.putText(
                    annotated_frame,
                    f"Intruders Visible: {current_intruders}",
                    (20, 105),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    annotated_frame,
                    f"Unique Intruders: {len(unique_intruder_ids)}",
                    (20, 140),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 0),
                    2
                )

                # ---------------- WRITE OUTPUT ----------------
                writer.write(annotated_frame)

                # ---------------- DISPLAY ----------------
                rgb_frame = cv2.cvtColor(
                    annotated_frame,
                    cv2.COLOR_BGR2RGB
                )

                video_placeholder.image(
                    rgb_frame,
                    channels="RGB",
                    use_container_width=True
                )

                # ---------------- PROGRESS ----------------
                if total_frames > 0:

                    progress_bar.progress(
                        min(frame_number / total_frames, 1.0)
                    )

                status_text.text(
                    f"Processing frame {frame_number} of {total_frames}"
                )

        finally:

            cap.release()
            writer.release()

        processing_time = time.time() - start_time

        # ---------------- RESULTS ----------------
        st.success("Monitoring completed successfully!")

        st.header("📊 Monitoring Results")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Unique Hen IDs",
            len(unique_hen_ids)
        )

        col2.metric(
            "Unique Intruders",
            len(unique_intruder_ids)
        )

        col3.metric(
            "Frames Processed",
            frame_number
        )

        col4.metric(
            "Processing Time",
            f"{processing_time / 60:.2f} min"
        )

        # ---------------- HEN RESULTS ----------------
        st.subheader("🐔 Hen Tracking")

        st.write(
            f"Unique hen tracking IDs: {len(unique_hen_ids)}"
        )

        st.write(
            f"Hen IDs: {sorted(unique_hen_ids)}"
        )

        # ---------------- INTRUDER RESULTS ----------------
        st.subheader("🚨 Intruder Tracking")

        if unique_intruder_ids:

            intruder_summary = Counter(
                class_name
                for class_name, track_id in unique_intruder_ids
            )

            st.write(
                f"Unique intruders detected: "
                f"{len(unique_intruder_ids)}"
            )

            for class_name, count in intruder_summary.items():

                st.write(
                    f"**{class_name.capitalize()}:** {count}"
                )

        else:

            st.success("No tracked intruders detected.")

        # ---------------- DOWNLOAD ----------------
        st.subheader("📥 Download Results")

        if os.path.exists(output_video):

            with open(output_video, "rb") as file:

                st.download_button(
                    label="Download Processed Video",
                    data=file.read(),
                    file_name="poultry_monitoring_output.mp4",
                    mime="video/mp4"
                )

        st.info(
            "Hen and intruder counts are based on unique tracking IDs. "
            "Tracking can still lose or change IDs when objects overlap, "
            "disappear or re-enter the frame. Detection is not guaranteed "
            "to be perfectly accurate."
        )

        # ---------------- CLEANUP ----------------
        try:
            os.remove(input_video)
        except OSError:
            pass
