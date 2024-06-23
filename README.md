# Binoculars - Object Detection with Video-to-Speech

   ```bash
88d8b.d8b.      88     88 
88'`88'`88`     88   88
88  88  88      88 8
88  88  88      88   88
88  88  88  88  88    88  88
   ```



This Python script demonstrates object detection using OpenCV's DNN module and provides spoken feedback using text-to-speech capabilities.

NOTE: you need to downlaod the yolov3.weights file (not included) to make the follwing code work. 


Introducing the revolutionary video-to-speech algorithm, designed to empower the visually impaired community! Using neural networks and video recognition libraries, we’ve created Binoculars to accurately describe visual content from videos in real-time. By converting visual information into clear and detailed spoken descriptions, our algorithm provides a seamless and immersive experience for users, enabling them to access a wide range of video content independently.

How does it work? Using Python, Binoculars splits the screen into blocks and analyzes each. As it analyzes it slowly makes inferences and can put the image back together. Using a list of requirements, it makes a conclusion of what the item is. It then grabs data from the position of the object and supposed distance to say it through a speaker, allowing for the user to be guided. 

Imagine effortlessly exploring educational videos, news clips, entertainment content, and more, with rich and descriptive audio narrations guiding your experience. Binoculars speaks to the user, guiding them through their everyday life, enhancing the depth and richness of the auditory experience.

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

## Next Steps

Something to note is that Binoculars is still in its early stages. The next steps would be to make the video recognition much more immersive and allow the audio assistant to actually have full description of what is in front of the user, rather than simply stating the object.


---

Maninder Kaur
