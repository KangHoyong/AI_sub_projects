import cv2
import numpy as np 

"""
Lucas-Kanade 방법은 희소 특성 집합에 대한 광학 흐름을 계산 
opencv 밀집한(dense) 광학 흐름을 찾기 위한 또 다른 알고리즘을 제공한다. (프레임의 모든 포인트에 대한 광학 흐름을 계산한다)

영상속의 움직임을 크기와 방향 , 2개의 채널, (u, v) 움직임의 방향은 방향에 해당하는 Hue(색상)값으로 이미지를 나타내고 
크기는 Value plane 으로 나타낸다. 

"""

cap = cv2.VideoCapture("ObjectTracking_code/videoDataset/vtest.avi") 
ret, frame1 = cap.read()
# image ch 1 : gray 
prev = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
print("hsv zeros_like test print \n"  , hsv )
hsv[...,1] = 255 

while(1):
    _, frame2 = cap.read()

    nexts = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev, nexts, None, 0.5,3,15,3,5,1.2,0)
    
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    print("mag \n" , mag)
    print("ang \n" , ang)
    
    # hav setting 
    test_hsv1 = hsv[...,0] = ang*180/np.pi/2
    test_hsv2 = hsv[...,2] = cv2.normalize(mag, None,0,255,cv2.NORM_MINMAX)
    
    print("test_hsv1 \n", test_hsv1)
    print("test_hsv2 \n", test_hsv2)

    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("test" , rgb)
    keyboard = cv2.waitKey(30) & 0xff 
    if keyboard == 27 :
        break
    elif keyboard == ord('s'):
        # svae code
        print("save test")
        cv2.imwrite("opticalfb.png" , frame2)
        cv2.imwrite("opticalhsv.png" , rgb)
    
cap.release()
cv2.destroyAllWindows()