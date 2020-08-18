# Background Subtraction 
# 백그라운드 이미지를 제거하고 원하는 물체만 남기는 예제 

import cv2 
import numpy as np 

cap = cv2.VideoCapture("ObjectTracking_code/videoDataset/highway.mp4")

# _, first_frame = cap.read() 

subtractor = cv2.createBackgroundSubtractorMOG2(history=25, varThreshold=35, detectShadows=True)

# Gray 
"""
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5) , 0)
""" 

while (1):

    _, frame = cap.read()

    mask = subtractor.apply(frame)

    cv2.imshow("frame" , frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(30) & 0xff
    if key == 27 : 
        break

    """
    구조
     vido -> frame -> cv2.cvtColor(Gray) -> GaussianBlur -> absdiff -> thershold
    # ret, frame = cap.read()
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5) , 0)
    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    cv2.imshow("First frame" , first_frame)
    cv2.imshow("Frame" , frame)
    cv2.imshow("differnce" , difference)

    key = cv2.waitKey(60) & 0xff
    if key == 27 : 
        break
    """ 

cap.release()
cv2.destroyAllWindows()