# fix 8/20 
import albumentations as A 
import random
import cv2
import os
from matplotlib import pyplot as plt

from albumentations.pytorch.transforms import ToTensorV2

from jsonUtility import jsonDataReadOneData

# global value 
# json_train_path = "./CarDataset/dataset/car_train/car_train.json" 

# fix code : test one image change more data 

# 파일 서치를 이용해서 모든 이미지를 가져와서 처리해보기 ... 또는 한 폴더만 조저서 해보기 !! 

imagePath = "./CarDataset/dataset/car_train/add_cctv/오송 사무실 1-20190927-092240-095240.mp4_snapshot_11.22_[2020.03.05_13.26.38].png" 

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

random.seed(7)

BOX_COLOR = (0,255,0) # gren
TEXT_COLOR = (255,255,255) # white 

def visualizeBBox(image, bbox, class_name , color=BOX_COLOR, thickness = 2) :

    # visualizes a single bounding box on the image 
    print("test debug : "  ,bbox, class_name)

    # image location and bbox
    x1, y1, x2, y2 = bbox
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    cv2.rectangle(image, (x1, y1), (x2, y2), color=color, thickness=thickness)

    # text location
    p1 = x1
    p2 = y1- 10 
    cv2.putText(image, class_name, (p1, p2), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,255,0), 2)
    return image

def visualizes(image , bboxes, category_ids, category_id_to_name) : 
    
    image = image.copy()
    for bbox, category_id in zip(bboxes, category_ids) : 
        class_name = category_id_to_name[category_id]
        image = visualizeBBox(image, bbox, class_name)

    cv2.imshow("windows", image)
    cv2.imwrite("transformsTestImage.png", image)
    if cv2.waitKey(0) & 0xFF == ord("q") : 
        exit()
    
    cv2.destroyAllWindows()
    return 0 

def main():

    # fileName, bbox, labels = jsonDataReadOneData(json_train_path)
    
    image = cv2.imread(imagePath)
    w, h = image.shape[:2]

    print("w , h debug -> ", w , h)
    # test 위해서 수동으로 입력 
    # 자동으로 가능하게 만들기 !! fix code
    bboxes = [[1061, 906, 1213, 963], [946, 664, 1920, 1080]]
    category_ids = [6, 1]
    category_id_to_name = {6 : "LicensePlate" , 1 : "Car"}

    # visualizes(image, bboxes, category_ids, category_id_to_name)

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
        category_id_to_name,
    )

if __name__ == "__main__":
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
