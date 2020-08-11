import torch 
import os 
# image 
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from imageRead import imageshowCv2, imageshowFIL



# image dataset dir
dir_path = "./dataset1/" 

# image save dir 
# 이미지 저장하기 위한 디렉토리 생성 [exist_ok = True] : 폴더가 없으면 생성 있으면 패스
os.makedirs("./0", exist_ok=True)
save_path = "./0/"

# image serarch 
def searchfile(dir_path, save_path, mode):
    print(dir_path)

    # try : 폴더 접근 권한이 없을경우 대비
    try : 
        file_names = sorted(os.listdir(dir_path))
        for file_name in file_names:
            full_filename = os.path.join(dir_path, file_name)
            # print("test image paht -> " , full_filename)
            if os.path.isdir(full_filename):
                """
                dataset1 
                  - 0 
                    |-- 0.jpg 
                  1.png
                  2.png 
                  하위 디렉토리 싹다 돌면서 이미지 파일 경로 찾아옴
                """
                searchfile(full_filename, save_path, mode) 
            else : 
                ext = os.path.splitext(full_filename)[-1]
                
                # 이미지 확장자 (png, jpg, jpeg ... 추가 가능)
                if ext == 'png' or 'jpg' or 'jpeg':
                    print("test png or jpg or jpeg" , full_filename)
                    #  이미지 파일을 보고 싶은경우 
                    # cv2 read and imag show
                    if mode == 'cv2' : 
                        imageshowCv2(full_filename , file_name, save_path)
                    elif mode == 'FIL':
                        imageshowFIL(full_filename, file_name, save_path)
                # jpg 파일만 처리하고 싶은경우
                # if full_filename.endswith(".jpg"):
                #     print("test jpg" , full_filename) 

    except PermissionError:
        pass

searchfile(dir_path, save_path, mode = 'cv2')
