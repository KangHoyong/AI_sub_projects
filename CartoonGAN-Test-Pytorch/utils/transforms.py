import cv2
import numpy as np 


# utils code 
def transformsShow(name = "img") :
    def transforms_show(img) : 
        cv2.imshow(name , np.array(img))
        if cv2.waitKey(0) & 0xff == ord('q') : 
            exit()
        return img 
    return transforms_show 

def show_image(img, name="img"):
    mean = np.array([0.485, 0.456, 0.406])
    std =  np.array([0.229, 0.224, 0.225])
    cv2.imshow(name, img.cpu().numpy().transpose((1,2,0)) * std + mean)
    if cv2.waitKey(0) & 0xff == ord('q') : 
            exit()