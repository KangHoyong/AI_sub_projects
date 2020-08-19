import json
import os 
import random
import argparse
import cv2

from pprint import pprint
from tqdm import tqdm
from PIL import Image 
# from detectron2.structures import BoxMode
# fix -> debug error : import _C x 
# custom test lib
from customUtility.jsonUtility import jsonDataRead
from customUtility.imageReadTest import oneImageTestOpen

imagePath = "./CarDataset/dataset/car_train/add_cctv/오송 사무실 1-20190927-092240-095240.mp4_snapshot_11.22_[2020.03.05_13.26.38].png" 
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

# fix : GPU 서버에 올려서 나머지 모듈 작성하기 !! 

def getCarDicts(json_train_path):

    datasetDicsts = []
    recode = {}

    fileName, bbox, labels, width, heigth = jsonDataRead(json_train_path)
    recode["file_name"] = fileName
    recode["width"] = width
    recode["height"] = heigth
    bboxs = bbox
    
    objs = [] 
    bboxsNumber = len(bboxs)
    for i in range(bboxsNumber) : 
    # x1, y1, x2, y2
        x1 = bboxs[i][0]
        y1 = bboxs[i][1]
        x2 = bboxs[i][2]
        y2 = bboxs[i][3]

        labelsNumber = labels[i]

        obj = {
            "bbox" : [x1, y1, x2, y2], 
            "category_id" : labelsNumber
        }
        objs.append(obj)
        recode["annotations"] = objs

        # print("recode" , recode)
        datasetDicsts.append(recode)
        # print("labelsNumber test " , labelsNumber)
        # print("bbox_number test " , bbox_number)
        # print("test customdataset \n" , filename)

    print("sample an example \n")
    pprint(random.sample(datasetDicsts, 3))


def main(config):
    # 8.18 fix : [code one image test code] 
    # jsonfile open 
    # jsonData = jsonOpen(config.json_train_path)
    # image Read
    # imgRead = oneImageTestOpen(imagePath)
    # json 필요한 data val 추출
    # fileName, bbox, labels = jsonDataRead(jsonData, imgRead)
    # drawBBox one image test code
    # drawBBoxOneImageTest(imgRead, fileName, bbox, labels, traget_classes)

    # detectron2 test code 
    getCarDicts(config.json_train_path)

if __name__ == "__main__":
    # test model parser 
    parser = argparse.ArgumentParser()

    # img path test
    parser.add_argument("--img_path" , type=str , default= "./CarDataset/dataset" , help= "img file path plz")

    # img cv2 and PIL read chose 
    parser.add_argument("--img_read_mode" , type=str, default="cv2", help="img_read_mode cv2 and FIL chose plz")

    # json train, val path test
    parser.add_argument("--json_train_path" , type=str , default= "./CarDataset/dataset/car_train/car_train.json" , help="json_train file path plz" )
    parser.add_argument("--json_val_path" , type=str, default="" , help="json_val file path plz")

    config = parser.parse_args()
    main(config)

