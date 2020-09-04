import matplotlib.pyplot as plt 
import cv2

def pltviewTest(orgImg, outputImg) : 
    img = orgImg
    outputImg = outputImg
    fig , axes = plt.subplots(1,2, figsize = (16,16))
    axes[0].imshow(img[:,:, :: -1])
    axes[1].imshow(outputImg[:,:, :: -1])
    plt.show()


def cv2viewTest(outputImg) : 
    img = outputImg
    cv2.imshow("View Test Windows" , img)
    if cv2.waitKey(0) & 0xff == ord('q') : 
        exit()


        