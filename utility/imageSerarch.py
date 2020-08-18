import argparse
import torch 
import os 
# image 
import cv2
from PIL import Image
import matplotlib.pyplot as plt

# image Read file
from imageRead import imageshowCv2, imageshowFIL



# image serarch 
def searchfile(dir_path, save_path, mode , imgTypeMode):

    # try : 폴더 접근 권한이 없을경우 대비
    try : 
        file_names = sorted(os.listdir(dir_path))
        for file_name in file_names:
            full_filename = os.path.join(dir_path, file_name)
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
                if full_filename.endswith(imgTypeMode) :
                    # cv2 read and imag show
                    if mode == 'cv2' : 
                        imageshowCv2(full_filename , file_name, save_path)
                        print("test code full_filename_path" , full_filename)
                    elif mode == 'FIL':
                        imageshowFIL(full_filename, file_name, save_path)
    except PermissionError:
        pass

def main(config):
    os.makedirs(config.img_save_dir_path, exist_ok=True)
    # image data search
    searchfile(config.img_path, config.img_save_dir_path, mode = config.img_mode ,imgTypeMode = config.img_type)


# main code test arge 
# ArgumentParser()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # imagePath and savePath 
    parser.add_argument("--img_path" , type=str , default="../dataset1", help="data")
    parser.add_argument("--img_save_dir_path" , type=str , default= "../0/", help="image save dir path")
    parser.add_argument("--img_save" , type=str , default="../0/" , help="data image save path")

    # image read mode cv2 and PIL 
    parser.add_argument("--img_mode" , type=str , default="cv2" , help="image read mode cv2 and pil")

    # image type chose 
    parser.add_argument("--img_type" , type=str , default=".jpg", help="imge tyep ex) jpg, png, jpeg, datafile type chose mode")


    config = parser.parse_args()
    main(config)