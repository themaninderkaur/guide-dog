# Binoculars - Object Detection with Text-to-Speech

This Python script demonstrates object detection using OpenCV's DNN module and provides spoken feedback using text-to-speech capabilities.

NOTE: you need to downlaod the yolov3.weights file (not included) to make the follwing code work. 

## Setup

1. Install the required libraries:
   - OpenCV (`cv2`)
   - NumPy (`numpy`)
   - pyttsx3 (`pyttsx3`)

2. Download the YOLOv3 model files (`yolov3.weights`, `yolov3.cfg`) and class names file (`name.names`).

3. Update the paths to the model weights, configuration file, and class names file in the code (`ObjectDetector` initialization).

## Usage

1. Run the script `object_detection.py`.
   ```bash
   python object_detection.py
   ```

2. The script will initialize the object detector and text-to-speech engine, then start capturing frames from the default camera.

3. Detected objects will be spoken out loud, and bounding boxes with labels and confidence levels will be displayed on the video feed.

4. Press 'q' to quit the application.

## Components

### ObjectDetector Class

- **`__init__(self, model_weights, model_config, class_names_file)`**: Initializes the object detector using YOLOv3 model files and loads class names from a file.
  
- **`detect_objects(self, frame)`**: Performs object detection on a frame, returning detected objects with labels, confidences, and bounding box coordinates.

### TextToSpeech Class

- **`__init__(self)`**: Initializes the text-to-speech engine.

- **`speak(self, text)`**: Converts text to speech and speaks it out loud.

## Dependencies

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- pyttsx3 (`pyttsx3`)

---

Maninder Kaur
