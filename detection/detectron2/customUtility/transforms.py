# fix 8/20 
import albumentations as A 
import random
import cv2
import os
from matplotlib import pyplot as plt

from albumentations.pytorch.transforms import ToTensorV2

from albumentationVis import visualizes
from jsonUtility import jsonDataReadOneData 

# global value 
json_train_path = "./CarDataset/dataset/car_train/car_train.json" 

# fix code : test one image change more data 

# 파일 서치를 이용해서 모든 이미지를 가져와서 처리해보기 ... 또는 한 폴더만 조저서 해보기 !! 

imagePath = "./CarDataset/dataset/car_train/add_cctv/오송 사무실 1-20190927-092240-095240.mp4_snapshot_11.22_[2020.03.05_13.26.38].png" 


def orgImageShow(imagePath) : 
    
    image = cv2.imread(imagePath)
    cv2.imshow("windows" , image)
    cv2.imwrite("orgImage.png", image)
    if cv2.waitKey(0) & 0xFF == ord("q") : 
        exit()


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

def main():

    fileName, bbox, labels = jsonDataReadOneData(json_train_path)
    
    image = cv2.imread(imagePath)
    w, h = image.shape[:2]

    print("w , h debug -> ", w , h)
    bboxes = bbox
    category_ids = labels

    bboxNumber = len(bboxes)
    for i in range(bboxNumber) : 

        labels_number = labels[i]
        labels_id = traget_classes[labels_number]

    print("debug >> " , labels_id)    
    category_id_to_name = labels_id

    transform = A.Compose(
        [
            # A.RandomSizedCrop(min_max_height=(1024,1024) , height=1080, width=1920, p=0.5),
            A.OneOf([
                A.HueSaturationValue(hue_shift_limit=0.2, sat_shift_limit=0.2, val_shift_limit=0.2, p=0.9),
                A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.9)
            ], p=0.9),
            A.HorizontalFlip(p=0.5),
            A.ShiftScaleRotate(p=0.5),            
        ],
        #  A.VerticalFlip(p=0.5),
        #  A.Cutout(num_holes=8, max_h_size=64 , max_w_size=64, fill_value = 0, p=0.5)],
        bbox_params=A.BboxParams(format="pascal_voc", label_fields=['category_ids']),
    )
    transformed = transform(image=image , bboxes=bboxes  ,category_ids=category_ids)
    visualizes(
        transformed['image'],
        transformed['bboxes'],
        transformed['category_ids'],
        category_id_to_name
    )

if __name__ == "__main__":
    # orgImageShow(imagePath)
    main()

# def getTrainTranforms() : 
#     return A.Compose([
#         A.ToGray(p=0.01),
#         A.HorizontalFlip(p=0.5),
#         A.VerticalFlip(p=0.5),
#         ToTensorV2(p=1.0)
#     ],
#     p = 1.0
#     bbox_params=A.BboxParams(
#         format="pascal_voc",
#         min_area= 0 ,
#         min_visibility=0, 
#         label_fields=['labels']
#     )
#     )

# def getValTranforms() : 
#     return A.Compose([
#         ToTensorV2(p=1.0)
#     ],
#     p = 0.1,
#     bbox_params= A.BboxParams(
#         format="pascal_voc",
#         min_area= 0, # 경계 상자의 최소 면적 
#         min_visibility= 0, # 경계 상자의 최소 면적 비율 
#         label_fields=["labels"]
#     )
#     )
