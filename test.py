import cvzone
import mediapipe
import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import random

cap=cv2.VideoCapture(0)
detector= HandDetector(maxHands=1)
startResult=False
startGame=False
timer=0
scores=[0,0]
while(True):
    imgBG=cv2.imread("Resources/BG.png")
    success, img=cap.read()
    imgScaled= cv2.resize(imgBG,(0,0),None,0.875,0.875)
    imgScaled=imgScaled[:,80:480]

    hands,img=detector.findHands(imgScaled)

    if(startGame):
        if startResult is False:
            timer=time.time()- initialTime
            cv2.putText(imgBG,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
            if timer>3:
                startResult=True
                timer=0

    


    if hands:
        playerMove=None
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        if fingers==[0,0,0,0,0]:
            playerMove=1
        if fingers==[1,1,1,1,1]:
            playerMove=2
        if fingers==[0,1,1,0,0]:
            playerMove=3
        print(fingers)

        randomNumber=random.randint(1,3)
        imgAI=cv2.imread(f'Resources/',cv2.IMREAD_UNCHANGED)
    Be    cvzone.overlayPNG(imgBG,imgAI,(149,310))
        print(playerMove)
    
    key=cv2.waitKey(1)
    if(key)==ord('s'):
        startGame=True
        initialTime=time.time()
        startResult=False
    cv2.imshow("image",img)
    cv2.imshow("BG",imgBG)
    cv2.imshow("Scaled",imgScaled)
    cv2.waitkey(1)
    

123