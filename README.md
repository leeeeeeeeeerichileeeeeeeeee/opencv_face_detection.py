# OpenCV Face Detection Project

A Python-based repository designed for architecture and construction students to explore image processing concepts through practical exercises in real-time face detection.

## Contents

1. **[Face Detection Script](opencv_face_detection.py)**  
   Detect faces in real-time using a webcam, with bounding boxes displayed around detected faces.

---

## **1. [Face Detection Script](opencv_face_detection.py)**

This project introduces architecture students to the basics of OpenCV through a practical exercise in image processing. The program captures real-time video from a webcam, detects human faces, and highlights them with bounding boxes. It’s designed for beginners to learn Python and OpenCV while applying programming skills to an architecture-related task.

#### Learning Objectives

- Learn the basics of OpenCV for image processing.
- Understand how to capture and process video frames in Python.
- Implement face detection using pre-trained Haar cascade classifiers.
- Apply image processing techniques in architectural contexts, such as smart systems.

#### Features

- **Real-Time Video Capture**: Access live video feed through a webcam.
- **Face Detection**: Utilize OpenCV's pre-trained Haar cascade classifier to detect faces in video frames.
- **Bounding Box Visualization**: Highlight detected faces with bounding boxes in real-time.
- **Interactive Control**: Exit the program by pressing the `q` key.

#### Tools & Libraries
- Python
- OpenCV (cv2 library)

#### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/opencv-face-detection.git
   cd opencv-face-detection
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python
   ```
3. Run the script:
   ```bash
   python opencv_face_detection.py
   ```
4. Exit the program:
   - Press the `q` key to quit the application.

#### Future Improvements
- Add support for detecting multiple facial features (e.g., eyes, smile).
- Implement a face recognition module to identify individuals.
- Include logging to track the number of detected faces over time.
- Integrate with architectural smart systems for interactive spaces.

---

