# fix 8/20 
import albumentations as A 
from albumentations.pytorch.transforms import ToTensorV2



def getTrainTranforms() : 
    return A.Compose([
        A.ToGray(p=0.01),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        ToTensorV2(p=1.0)
    ],
    p = 1.0
    bbox_params=A.BboxParams(
        format="pascal_voc",
        min_area= 0 ,
        min_visibility=0, 
        label_fields=['labels']
    )
    )

def getValTranforms() : 
    return A.Compose([
        ToTensorV2(p=1.0)
    ],
    p = 0.1,
    bbox_params= A.BboxParams(
        format="pascal_voc",
        min_area= 0, # 경계 상자의 최소 면적 
        min_visibility= 0, # 경계 상자의 최소 면적 비율 
        label_fields=["labels"]
    )
    )
