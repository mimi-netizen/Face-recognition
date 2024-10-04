import cv2
import numpy as np
import sqlite3

# Load the pre-trained face detector
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # to detect faces in camera
cam = cv2.VideoCapture(0)  # 0 is for web camera

def insertorupdate(Id, Name, age):  # function to manage sqlite database
    conn = sqlite3.connect("sqlite.db")  # connect to database
    cmd = "SELECT * FROM STUDENTS WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)  # cursor to execute statement
    isRecordExist = 0  # assume there is no record in our table
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        conn.execute("UPDATE STUDENTS SET Name=? WHERE Id=?", (Name, Id,))
        conn.execute("UPDATE STUDENTS SET age=? WHERE Id=?", (age, Id,))
    else:
        conn.execute("INSERT INTO STUDENTS (Id, Name, age) values(?, ?, ?)", (Id, Name, age))

    conn.commit()
    conn.close()

# Insert user-defined values into table
Id = input('Enter User Id: ')
Name = input('Enter User Name: ')
age = input('Enter User age: ')

insertorupdate(Id, Name, age)

# Detect face in web camera
sampleNum = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum += 1  # Increment sample number
        cv2.imwrite("dataset/user." + str(Id) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)
    cv2.imshow("Face", img)
    cv2.waitKey(1)
    if sampleNum > 20:  # Stop after collecting 20 samples
        break

cam.release()
cv2.destroyAllWindows()
