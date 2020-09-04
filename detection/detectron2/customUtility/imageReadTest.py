import cv2
import os
from tqdm import tqdm

# one image test code 
def oneImageTestOpen(imagePath):
    imgRead= cv2.imread(imagePath)

    return imgRead


# dirData search code
def searchfile(dirPath, mode) :
    try:
        fileNames = sorted(os.listdir(dirPath))
        for fileName in tqdm(fileNames) : 
            fullFileName = os.path.join(dirPath, fileName)
            if os.path.isdir(fullFileName):
                """
                dataset1 

                train 
                   0 - img 
                   1 - img 
                   0 - 0
                  - 0 
                    |-- 0.jpg 
                  1.png
                  2.png 
                  하위 디렉토리 싹다 돌면서 이미지 파일 경로 찾아옴
                """
                searchfile(fullFileName,mode)
            else : 
                # fix code image type 8/19일 
                ext = os.path.splitext(fullFileName)[-1]
                print(ext)
                if ext != ".DS_Store" :  
                    if mode == "cv2" : 
                        return fullFileName

    except PermissionError:
        pass

def getImageIds(imageFolder = None):
    """
    Explores a folder of image and get their ID from their file name
    Return a list of all image ID's image_folder 
    """
    # imageFolder = imgPath + imgName
    if imgName.endswith(".jpg") : 
        return [os.path.splitext(imgName)[0] for imgName in sorted(os.listdir(imageFolder + imgName))]


if __name__ == "__main__":
    
    oneImageTestOpen(imagePath)