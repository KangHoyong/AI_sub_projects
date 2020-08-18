import cv2
import numpy as np 

# video open 
cap = cv2.VideoCapture("ObjectTracking_code/videoDataset/vtest.avi")

# ShiTomasi 코너 탐지를 위한 파라미터 
feature_parmes = dict(
    maxCorners = 100, 
    qualityLevel = 0.3, 
    minDistance = 7,
    blockSize = 7
)

# Lucass Kanade 광학 흐름을 위한 파라미터 
lk_params = dict(
    winSize = (15,15), 
    maxLevel = 2, 
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10 , 0.3)
)

# 랜덤 색 생성하기 
color = np.random.randint(0, 255, (100, 3))

# 1st frame 코너 찾기
ret , f_frame = cap.read()
f_frame_gray = cv2.cvtColor(f_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(f_frame_gray, mask=None, **feature_parmes)
print("f_frame test " , f_frame.shape)
# 그리기 위해서 마스크 이미지 생성

mask = np.zeros_like(f_frame)
print("mask test print : " , mask.shape)

while(1):
    ret, frame = cap.read()
    # image color = gray 
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # opticalFlow 계산 
    p1 , st , err = cv2.calcOpticalFlowPyrLK(f_frame_gray, frame_gray, p0, None, **lk_params)

    # point 선택 
    point_frame_gray = p1[st == 1]
    point_f_frame = p0[st == 1]

    # 추적 하고 그리기 
    # fix after_frame : new_frame , befor_frame : old_frame 
    for i, (after_frame , befor_frame) in enumerate(zip(point_frame_gray, point_f_frame)):
        x1, y1 = after_frame.ravel()
        print("x1 , y1 val print test code  : " , x1, y1)
        x2, y2 = befor_frame.ravel()
        print("x2, y2 value print test code : " , x2, y2)
        mask = cv2.line(mask, (x1, y1) , (x2, y2) , color[i].tolist(), 2)

        # 5 frame 마다 특징점을 찾는 샘플을 제공한다. 또한 광학 흐름 포인트를 역 확인해서(Backward_check) 좋은 점만 선택
        frame = cv2.circle(frame, (x1, y1) , 1, color[i].tolist(), -1)
    

    print("frame test size : " , frame.shape)
    print("mask test size : " , mask.shape)
    img = cv2.add(frame, mask)
    cv2.imshow("windows" , img)
    keyboard = cv2.waitKey(30) & 0xff 
    if keyboard == 27 : 
        break

    # 이전 프레임과 이전 포인트 업데이트 추적 하기 
    befor_frame = frame_gray.copy()
    p0 = point_frame_gray.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()


