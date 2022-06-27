import cvzone
import mediapipe
import cv2


cap=cv2.VideoCapture(0)
while (True):
    success, img=cap.read()
    cv2.imshow("image",img)
    cv2.waitkey(1)
