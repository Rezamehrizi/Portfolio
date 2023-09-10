import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained MobileNetV2-based object detection model
detection_model = cv2.dnn_DetectionModel('frozen_inference_graph.pb', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')

# Define a list to store class labels
class_labels = []

# Read class labels from a 'labels.txt' file
labels_file = 'labels.txt'
with open(labels_file, 'rt') as file:
    class_labels = file.read().rstrip('\n').split('\n')

# Set input parameters for the model
detection_model.setInputSize(320, 320)
detection_model.setInputScale(1.0/127.5)
detection_model.setInputMean((127.5, 127.5, 127.5))
detection_model.setInputSwapRB(True)

# Read an input image ('image1.png') for object detection and display it using Matplotlib
input_image = cv2.imread('image1.png')
plt.imshow(input_image)

# Perform object detection on the image with a confidence threshold of 0.5
class_indices, confidence_scores, bounding_boxes = detection_model.detect(input_image, confThreshold=0.5)

# Set font properties for labels and boxes
font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

# Loop through detected objects and draw bounding boxes with class labels and confidence scores
for class_index, confidence, box in zip(class_indices.flatten(), confidence_scores.flatten(), bounding_boxes):
    cv2.rectangle(input_image, box, (255, 0, 0, 2))
    cv2.putText(input_image, class_labels[class_index - 1], (box[0]+10, box[1]+40), font, fontScale=font_scale, color=(0, 255, 0), thickness=3)

# Display the image with detected objects using Matplotlib
plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))

# Open a video capture from 'video1.mp4' or the default camera
video_capture = cv2.VideoCapture('video1.mp4')
if not video_capture.isOpened():
    video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    raise IOError('Cannot open the video')

# Set font properties for labels and boxes in the video frames
font_scale = 2

# Process each frame in the video
while True:
    ret, video_frame = video_capture.read()  # Read the current frame from the video
    video_frame = cv2.resize(video_frame, (0, 0), fx=0.5, fy=0.5)  # Resize the frame

    # Perform object detection on the frame with a confidence threshold of 0.55
    class_indices, confidence_scores, bounding_boxes = detection_model.detect(video_frame, confThreshold=0.55)

    # Check if any objects are detected
    if len(class_indices) != 0:
        for class_index, confidence, box in zip(class_indices.flatten(), confidence_scores.flatten(), bounding_boxes):
            if class_index <= 80:  # Filter objects up to class 80 (adjust as needed)
                cv2.rectangle(video_frame, box, (255, 0, 0, 2))
                cv2.putText(video_frame, class_labels[class_index - 1], (box[0]+10, box[1]+40), font, fontScale=font_scale, color=(0, 255, 0), thickness=3)
    
    # Display the frame with detected objects
    cv2.imshow('Object Detection', video_frame)
    
    # Exit the video loop when 'q' is pressed
    if cv2.waitKey(2) & 0xff == ord('q'):
        break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()