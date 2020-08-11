import numpy as np 
# data augmentation 
# [1] : randomRsizeCrop

def imageRandomRsizeCrop(img, new_h, new_w):
    h, w = img.shape[:2]
    print("h" , "w", w, h)
    top = np.random.randint(0, h - new_h)
    print("test top val = " , top)
    left = np.random.randint(0, w - new_w) 
    print("test left val = ", left )

    img = img[top : top + new_h , left: left + new_w]

    return img
