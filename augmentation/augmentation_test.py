import numpy as np 
import cv2

# 체크 글로벌 라이브러리 관리 되는지 확인하기 !! fix 

# data augmentation 
# [1] : randomRsizeCrop

# imge RandomRsizeCrop
def imageRandomRsizeCrop(img, new_h, new_w):
    h, w = img.shape[:2]
    print("h" , "w", w, h)
    top = np.random.randint(0, h - new_h)
    print("test top val = " , top)
    left = np.random.randint(0, w - new_w) 
    print("test left val = ", left )

    img = img[top : top + new_h , left: left + new_w]

    return img

# brightness  
# brightness : 명도 , contrast 대비
def brightnessImage(img, brightness, contrast) : 
    print("img test : \n" , img )
    img = np.int16(img)
    print("img test int16 : \n", img)
    img = img * (contrast / 127 + 1) - contrast + brightness
    img = np.clip(img, 0 , 255)
    img = np.uint8(img)

    return img

# imge resize 
def imgeResize(img , dsizeH, dsizeW) : 
    img = cv2.resize(img, dsize=(dsizeH, dsizeW))
    # fix
    resizeHeight ,resizeWidth = img.shape[:2]
    print(img)

    return img