import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml'); #to detect faces in camera
cam=cv2.VideoCapture(0); #0 is for web camera

def insertorupdate(Id,Name,age):            #function is for sqlite database
    conn=sqlite3.connect("database.db")     #connect database
    cmd="SELECT * FROM STUDENTS WHERE ID="+str(Id);
    cursor=conn.execute(cmd);               #cursor to execute statement
    isRecordExist=0;                        #assume there is no record in our table
    for row in cursor:
        isRecordExist=1;
    if(isRecordExist==1):
        conn.execute("UPDATE STUDENTS SET Name=? WHERE Id=?",(Name,Id,))
        conn.execute("UPDATE STUDENTS SET age=? WHERE Id=?", (age,Id,))
    else:
        conn.execute("INSERT INTO STUDENTS (Id,Name,age) values(?,?,?)",(Id,Name,age))

    conn.commit()
    conn.close()

#insert user defined values into table
Id=input('Enter User Id')
Name=input('Enter User Name')
age=input('Enter User age')

insertorupdate(Name,Id,age)

#detect face in web camera
sampleNum=0
while(True):
    ret,img=