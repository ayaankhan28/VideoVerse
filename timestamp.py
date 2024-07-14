import cv2
import json
from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO('./model/best.pt')  # Replace with your model path

# Open the video file
video_path = "C:\\Mydrive\\DL\\pepsi3.avi"
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)

# Dictionaries to hold timestamps for each class
timestamps = {
    'Pepsi_pts': [],
    'CocaCola_pts': []
}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Get the current frame number
    frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)

    # Perform inference
    results = model(frame)

    # Process results
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extract bounding box coordinates
            conf = box.conf[0]  # Confidence score
            cls = int(box.cls[0])  # Class label
            label = f'{model.names[cls]} {conf:.2f}'

            if model.names[cls] == 'Pepsi':  # Check if the detected class is Pepsi
                # Calculate the timestamp
                timestamp = frame_number / fps
                timestamps['Pepsi_pts'].append(timestamp)
                print(f'{model.names[cls]} detected at {timestamp:.2f} seconds')

            elif model.names[cls] == 'Cola':  # Check if the detected class is CocaCola
                # Calculate the timestamp
                timestamp = frame_number / fps
                timestamps['CocaCola_pts'].append(timestamp)
                print(f'{model.names[cls]} detected at {timestamp:.2f} seconds')

    # Display the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Write the timestamps to a JSON file
with open('timestamps.json', 'w') as f:
    json.dump(timestamps, f, indent=4)

print("Timestamps saved to timestamps.json")
