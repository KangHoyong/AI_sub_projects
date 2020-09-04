import numpy as np
from matplotlib import pyplot as plt
import cv2
import matplotlib
import glob
import os
import argparse

# 8월 28일
# fix code .npy -> image png file svae 

# image serarch 
def searchfile(dir_path , save_path):

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
                searchfile(full_filename, save_path) 
            else : 
                ext = os.path.splitext(full_filename)[-1]
                if full_filename.endswith(".npy") :
                    imgArray = np.load(full_filename, allow_pickle=True)
                    print(full_filename)
                    os.makedirs(save_path , exist_ok=True)
                    path = os.path.join(save_path, file_name + ".png")
                    matplotlib.image.imsave(path, imgArray)
              
    except PermissionError:
        pass


def main(config) : 
    searchfile(config.numpydata_path, config.save_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # numpydata file MOT16_POl_train (MOT16-02.npy)
    parser.add_argument("--numpydata_path" , type=str, default="../MOT16_POI_train" , help="numpydata path plz")
    
    # file save dir path 
    parser.add_argument("--save_path" , type=str , default="./0" , help="data save path plz")

    config = parser.parse_args()
    main(config)