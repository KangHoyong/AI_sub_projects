import cv2
import os
import numpy as np
from PIL import Image

# sys
# paht

# fix code 8/15 
# python 외부 라이브러리 적용 오류 수정하기
"""
import sys
sys.path.append(("/augmentation"))
print("sys : " , sys.path)
from augmentation_test import imageRandomRsizeCrop
""" 

def imageshowCv2(img_path, file_name , save_path):
    print("2 : " , img_path)
    img = cv2.imread(img_path)
    print("3 : " , save_path)
    
    # augmentation_test_code 
    # img = imageRandomRsizeCrop(img, 800, 800)
    """
    new_h = 500
    new_w = 500
    h, w = img.shape[:2]
    print("h" , "w", w, h)
    print("NewHeight, NewWidth" , new_h, new_w)
    top = np.random.randint(0, h - new_h)
    print("test top val = " , top)
    left = np.random.randint(0, w - new_w) 
    print("test left val = ", left )
    img = img[top : top + new_h , left: left + new_w]
    """
    # show test code 
    print(img.shape)
    cv2.imshow("windows" , img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        exit()
    # cv2 save 해야하는경우 
    img_save_path = save_path + f"{file_name}.png"
    print("print test -> " , img_save_path)
    cv2.imwrite(img_save_path, img)

    return img

def imageshowFIL(img_path, file_name, save_path):
    print("test 1 code") 
    img = Image.open(img_path)
    # show test code
    # img.show()
    img_save_path = save_path + f"{file_name}.png"
    img.save(img_save_path, 'JPEG')


    