import cv2 

# cv2 video open 
cap = cv2.VideoCapture("ObjectTracking_code/videoDataset/vtest.avi")

"""
frame - background model - > (>) Threshold -> foreground mask 
createBackgroundSubtractorMOG2
 - 가우시안 믹스쳐 기반의 배경 / 전경 분할 알고리즘이다. 이 알고리즘의 한 가지 중요한 특성은 각 픽셀에 대해 알맞는 가우시안 분포의 수를 선택한다는 것이다.
 기존 MOG 에서는 k 가우시안 분포를 가졌다 이는 조명변화로 인한 다양한 장면에 대해서 더 나은 적응력을 보인다. 
"""

# detectShadows -> 그림자 색상 그레이 또는 흰색 
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
fgdg = cv2.createBackgroundSubtractorMOG2()
# while 
while(1) : 
    ret , frame = cap.read()

    frame = cv2.resize(frame, (400,400))
    print("ret test print : " , ret)
    print("frame test print : " , frame)

    # 만약에 read 안된다면 종료 
    if frame is None : 
        break

    fgmask = fgdg.apply(frame)
    # 노이즈 제거 closing and opening 과 같은 몇몇 형태학적인 (morphological) 필터링으로 원하지 않는 노이즈를 제거 
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow("Windows" , frame)
    cv2.imshow("FG MASK Frame" , fgmask)
    keyboard = cv2.waitKey(30) & 0xff
    if keyboard == 27 : 
        break


cap.release()
cv2.destroyAllWindows()

