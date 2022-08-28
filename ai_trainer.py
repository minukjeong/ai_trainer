import cv2
import numpy as np
import mediapipe as mp
import pose_detection as pm
import time


cap = cv2.VideoCapture('C:/Users/gram/Desktop/image/bicepcurl.mp4')

if not cap.isOpened():
    print("could not video")
    exit()

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    ret, frame = cap.read()
#    frame = cv2.resize(frame, (1280,720))

#    img = cv2.imread("C:/Users/gram/Desktop/image/img.jpg")
    img = detector.findpose(frame)
#    img = detector.findpose(img, False)
    lmList = detector.findPosition(img, False)
    #print(lmList)
    if len(lmList) != 0:
        #Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        #Left Arm
        #detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle,(160, 13), (0, 100))
        bar = np.interp(angle,(155,20), (650,100))
        #print(angle, per)

        #check for thr dumbbel curls

        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1

        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0

        print(count)



        # cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
        #             (255, 0, 0), 5)

        cv2.rectangle(img, (500, 100), (600, 650), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (400, 80), cv2.FONT_HERSHEY_PLAIN,4,
        (255,0,0),4)

        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

    cv2.imshow("AI", frame)
    cv2.waitKey(1)
