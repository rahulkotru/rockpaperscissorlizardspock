import cvzone
import mediapipe
import cv2


cap=cv2.VideoCapture(0)

while (True):
    imgBG= cv2.imread("Resources/rock.png")
    imgScaled= cv2.resize(imgBG,(0,0),None,0.875,0.875)
    imgScaled=imgScaled[:,80:480]
    imgBG[]=
    success, img=cap.read()
    cv2.imshow("image",img)
    cv2.imshow("BG",imgBG)
    cv2.imshow("Scaled",imgScaled)
    cv2.waitkey(1)
