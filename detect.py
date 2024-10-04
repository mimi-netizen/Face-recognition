import cv2
import numpy as np
import os
import sqlite3

# Load the Haar Cascade for face detection
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
if facedetect.empty():
    raise ValueError("Error loading Haar Cascade.")

# Start video capture
cam = cv2.VideoCapture(0)

# Load the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
try:
    recognizer.read("recognizer/trainingdata.yml")
except Exception as e:
    raise ValueError(f"Error loading training data: {e}")

def get_profile(user_id):
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.execute("SELECT * FROM STUDENTS WHERE id=?", (user_id,))
    profile = cursor.fetchone()  # Fetch a single profile
    conn.close()
    return profile

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        user_id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        profile = get_profile(user_id)

        if profile is not None:
            cv2.putText(img, "Name: " + str(profile[1]), (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
            cv2.putText(img, "Age: " + str(profile[2]), (x, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)

    cv2.imshow("FACE", img)

    if cv2.waitKey(1) == ord('q'):  # Exit on 'q'
        break

# Release camera and close windows
cam.release()
cv2.destroyAllWindows()