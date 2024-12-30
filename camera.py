import cv2
from detection import AccidentDetectionModel
import numpy as np
from alert import send_alert

# Initialize the accident detection model
accident_model = AccidentDetectionModel(r"C:\Users\tharu\Downloads\pro\project\model.json", r"C:\Users\tharu\Downloads\pro\project\model_weights.keras")
font_style = cv2.FONT_HERSHEY_SIMPLEX

def run_application():
    video_capture = cv2.VideoCapture(r"D:\SVMCE hackathon\accident1\Accident-Detection\car24.mp4") 
    alert_sent = False  # Flag to track if alert has been sent
    frame_skip = 5  # Number of frames to skip for faster processing
    frame_count = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized_frame = cv2.resize(rgb_frame, (250, 250))
 
        prediction, probability = accident_model.predict_accident(resized_frame[np.newaxis, :, :])
        if prediction == "Accident" and not alert_sent:
            send_alert("Accident detected")
            alert_sent = True  # Set the flag to True after sending the alert
            probability = round(probability[0][0] * 100, 2)
            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, f"{prediction} {probability}", (20, 30), font_style, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
        cv2.imshow('Video', frame)  
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_application()