import cv2
import numpy as np
import pyttsx3

class ObjectDetector:
    def __init__(self, model_weights, model_config, class_names_file):
        self.net = cv2.dnn.readNet(model_weights, model_config)
        with open(class_names_file, 'r') as f:
            self.classes = f.read().splitlines()

    def detect_objects(self, frame):
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        output_layers_names = self.net.getUnconnectedOutLayersNames()
        layerOutputs = self.net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        detections = []
        if len(indexes) > 0:
            for i in indexes.flatten():
                label = str(self.classes[class_ids[i]])
                confidence = round(confidences[i], 2)
                detections.append((label, confidence, boxes[i]))

        return detections

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    detector = ObjectDetector('MyApp/yolov3.weights', 'MyApp/yolov3.cfg', 'MyApp/name.names')
    tts = TextToSpeech()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        detections = detector.detect_objects(frame)

        for detection in detections:
            label, confidence, (x, y, w, h) = detection
            text = f"{label} detected with confidence {confidence}"
            tts.speak(text)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
