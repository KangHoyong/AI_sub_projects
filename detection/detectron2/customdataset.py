import json
import os 
import random
import argparse
import cv2

from pprint import pprint
from tqdm import tqdm
from PIL import Image 

# from detectron2.detectron2.structures import BoxMode
#fix 8/18일 
# Utility make moduel add 
# add befor 

# test moduel path 
"""
본인이 지정한 위치 경로 넣어줄것
img_path : "./dataset"
json_train_path : "car_train.json"
json_val_path : "car_val.json"
"""
# traget_classes : _background_ , car, suv, van, truck, specialCar, licensePlate, Person, Motorcycle 

# trage_classes = "_background_" why add ? -> two stage json file (two stage background -> add)
# One Stage = no background solution is add _background_ or [json[lables] value - 1 == traget_class number]  
traget_classes = [
    "_background_",
    "Car",
    "Suv",
    "Van",
    "Truck",
    "SpecialCar",
    "LicensePlate",
    "Person",
    "Motorcycle"
]
print(traget_classes)

def getJsonfileRead(json_train_path, imgPath) : 

    # fix 8월 18일 = PM 05 : 40 
    # img bbox test code [1]
    img = cv2.imread("./CarDataset/dataset/car_train/add_cctv/오송 사무실 1-20190927-092240-095240.mp4_snapshot_11.22_[2020.03.05_13.26.38].png")
    cv2.imshow("windows" , img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        exit()
    
    jsonData = []
    with open(json_train_path) as f : 
        jsonData = json.load(f)

    print("Json data file one test print \n")
    pprint(jsonData[0])

    # data annotation one file test code 
    annotations = jsonData[0]
    fileNameTest = annotations["filename"]
    annos = annotations["ann"]
    bbox = annos["bboxes"]

    # one image : bbox number (one image with MultiBBox)
    bboxNumber = len(bbox) 
    for i in range(bboxNumber) :
        # ex ) [0,0,0,0] 
        x1 = bbox[i][0]
        y1 = bbox[i][1]
        x2 = bbox[i][2]
        y2 = bbox[i][3]

        print(x1, y1, x2 ,y2)
        lables = annos["labels"]
        lablesNumber = lables[i]
        
        # imgLablesId = lablesNumber - 1
        
        print(lablesNumber)


# fix image show bbox test code [0]  


"""
    for annotations in jsonData : 
        recode = {}
        fileNaem = annotations["filename"]
        annos = annotations["ann"]
        bbox = annos["bboxes"]

        # pprint(bbox)
        numBBox = len(bbox)
        # print("numBBox len :" , numBBox)
        
        for i in range(numBBox) : 
            fileNaem = annotations["filename"]
            # print(fileNaem)
            bbox  = annos["bboxes"] 

            # pprint(bbox)
            # [x1, y1 , x2 , y2]
            x1 = bbox[i][0]
            y1 = bbox[i][1]
            x2 = bbox[i][2]
            y2 = bbox[i][3] 

            # print(x1, y1 , x2 ,y2)
        
            lables = annos["labels"]
            # print(lables)           
            lables_number = lables[i]
            # print(lables_number)
            image_id = lables_number
            
 """
# image file name 1111.jpg -> 1111
def getImageIds(imageFolder = None):
    """
    Explores a folder of image and get their ID from their file name
    Return a list of all image ID's image_folder 

    """
    # imageFolder = imgPath + imgName
    if imgName.endswith(".jpg") : 
        return [os.path.splitext(imgName)[0] for imgName in sorted(os.listdir(imageFolder + imgName))]

# json file test code 
# def jsonSearchfile() : 


# image file test code 
# input imagePath , mode = cv2 and PIL , imgTypeMode = chose (jpg, png, jpeg)
def searchfile(dirPath, mode) :
    try:
        fileNames = sorted(os.listdir(dirPath))
        for fileName in tqdm(fileNames) : 
            fullFileName = os.path.join(dirPath, fileName)
            if os.path.isdir(fullFileName):
                """
                dataset1 
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
                        imageShowCv2(fullFileName, fileName)

    except PermissionError:
        pass

# cv2 image box cheack 
def imageShowCv2(fullFileName, fileName) : 

    # input fileName : save 하는경우 사용 예정 
    img = cv2.imread(fullFileName)
    # show test code [1 folder] 
    # sample data path : ./CarDataset/dataset/car_train/크롤링_차종이미지/승용차
    # cv2.imshow("windows" , img)
    if cv2.waitKey(0) & 0xFF == ord('q') : 
        exit()
    # output img
    return img

def main(config):
    # searchfile(config.img_path,config.img_read_mode)
    getJsonfileRead(config.json_train_path , config.img_path)


if __name__ == "__main__":
    # test model parser 
    parser = argparse.ArgumentParser()

    # img path test
    parser.add_argument("--img_path" , type=str , default= "./CarDataset/dataset" , help= "img file path plz")
    # test sample img show path 
    # parser.add_argument("--img_path" , type=str , default= "./CarDataset/dataset/car_train/크롤링_차종이미지/승용차" , help= "img file path plz")

    # img cv2 and PIL read chose 
    parser.add_argument("--img_read_mode" , type=str, default="cv2", help="img_read_mode cv2 and FIL chose plz")

    # json train, val path test
    parser.add_argument("--json_train_path" , type=str , default= "./CarDataset/dataset/car_train/car_train.json" , help="json_train file path plz" )
    parser.add_argument("--json_val_path" , type=str, default="" , help="json_val file path plz")

    config = parser.parse_args()
    main(config)

