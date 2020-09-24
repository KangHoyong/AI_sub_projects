# AI_sub_projects
AI_sub_projects and Study 

### Detectron2 with Pytorch and customDataset 

### CartoonGAN Test code with Pytorch (web <-> model)

리엑트 + TS

test server 구성 : local server 

클라이언트 
web -> input image -> server -> output image -> view(result image)

서버 
input image -> CartoonGan Model -> output image (web)  


### Simple Python Version Management install 
Simple Python Version Management install [install page](https://github.com/KangHoyong/AI_sub_projects/issues/4)

### 논문 정리 

Feature Pyramid [review](https://github.com/KangHoyong/AI_sub_projects/issues/1)

# 논문 리스트 (매일 업데이트 됨)

### 이미지 분류 분야
image Classification [Paper list](https://paperswithcode.com/sota/image-classification-on-imagenet)

### 객체 검출 분야 
객체 검출 분야 [Paper list](https://paperswithcode.com/sota/object-detection-on-coco)

### 세그멘테이션 
세그멘테이션 [Paper list](https://paperswithcode.com/sota/semantic-segmentation-on-cityscapes)

### Action recognition 
Action recognition [Paper list](https://paperswithcode.com/task/action-classification)


### intelrealsense 

1. 영상을 받아와서 뿌려 주는 부분을 체크 하고 
2. depth , rgb API 영상 가져오기 
3. 위치 맞추기 보는 시야각이 depth 랑 rgb랑 다름 
4. 녹화 하기 / 녹화 되고있는지 확인하는 창 만들기 
5. 저장 위치 지정하기 temp 생성 해서 거기에 저장하기 저장 이름은 depth_cam_{auto number}.mp4


1. depth와 rgb 위치가 정확하게 맞아야됨
 depth가 일반적으로 시야각이 넓으므로 rgb와 맞추기 위해선 crop 해야됨 (RealSense API 에서 기능 제공)
2. depth를 일반적으로 뽑으면 1 차원으로 거리 z로 데이터가 나오는데 이걸 jet / white and black 2가지로 뽑아야됨


3. 카메라가 제대로 녹화가 되고 있는지 보여주는 visualize 하는 창 필요 (cv2)처럼 대신 이때는 rgb 카메라만 보여주면 됨 굳이 depth까지 visualize 할 필요 없음


즉 최종적으로 저장될 때는
1. depth Jet / white and balck 2가지
2. rgb로 저장

저장 할 때는 위의 해상도 옵션으로 저장 될 것
물론, depth 같은 경우 rgb랑 시야각 맞추다 보면 crop 되므로 실제론 848x480보다 작을 것임
