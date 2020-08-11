import cv2
import os
from PIL import Image

# sys
# paht
import sys
sys.path.append(("/augmentation"))
print("sys : " , sys.path)
from augmentation_test import imageRandomRsizeCrop

# import imageRandomRsizeCrop

def imageshowCv2(img_path, file_name , save_path):
    print("2 : " , img_path)
    img = cv2.imread(img_path)
    
    # augmentation_test_code 
    img = imageRandomRsizeCrop(img, 800, 800)

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


    