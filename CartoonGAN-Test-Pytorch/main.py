import torch
import torchvision.transforms as transforms 
import cv2
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt  
import torchvision.utils as vutils

from network.Transformer import Transformer
from utils.transforms import transformsShow
from utils.viewTest import pltviewTest, cv2viewTest

# image type list 
imageType_ext = [".jpg" , ".png"]

# fix code file open 처리하기 지속적으로 처리하기 !! 
def test(img, img_save_path , file_name) : 
    model = Transformer()
    model.load_state_dict(torch.load("./pretrained_model/Hayao_net_G_float.pth"))
    model.eval()

    print("Model loading !!") 
    img_size = 450    

    # image test path 
    # img_paht = "./test_img/5--26.jpg"
    
    img = cv2.imread(img)

    T = transforms.Compose([
        transforms.ToPILImage(), 
        transforms.Resize(img_size, 2),
        # transformsShow("Windows_test" ),
        transforms.ToTensor()
    ])
    img_input = T(img).unsqueeze(0)
    img_input = -1 + 2 * img_input # 0 - 1 -> -1 - +1
   
    
    # forward 
    img_output = model(img_input)

    img_output = (img_output.squeeze().detach().numpy() + 1.) / 2.
    # [3, 452 , 672]
    print("test image >> " , img_output.shape) 
    img_output = img_output.transpose([1,2,0])

    # 
    print("transpose >> " , img_output)
    # [452, 672, 3]
    
    # pltviewTest(img, img_output)
    cv2viewTest(img_output)

    # img_output = img_output[0]
    # deprocess, (0, 1)
    # img_output = img_output.data.cpu().float() * 0.5 + 0.5

    saveFile(img_output, img_save_path ,file_name)



def saveFile (outImg, img_save_path , file_name) : 

    # save fix code 
    print("outputImg info >> " , outImg.shape)
    # save dir 있는가 없는가 판단하고 없으면 생성 있으면 패스 ..
    os.makedirs(img_save_path , exist_ok=True)

    # image save code 
    # file_name[-4] : ex -> image.png -> imgae 
    img_path = os.path.join(img_save_path , file_name[:-4] + ".png")

    print("img_path debug code >> ", img_path)

    # vutils.save_image(outImg, img_path)
    cv2.imwrite(img_path, outImg)
    
def searchfile(dir_path , save_path):

    # try : 폴더 접근 권한이 없을경우 대비
    try : 
        file_names = sorted(os.listdir(dir_path))
        for file_name in file_names:
            full_filename = os.path.join(dir_path, file_name)
            print("dubug full_filename >> " , full_filename)
            print("debug file name >> " , file_name)
            if os.path.isdir(full_filename):
                """
                dataset1 
                  - 0 
                    |-- 0.jpg 
                  1.png
                  2.png 
                  하위 디렉토리 싹다 돌면서 이미지 파일 경로 찾아옴
                
                """
                searchfile(full_filename, save_path) 
            else : 
                ext = os.path.splitext(full_filename)[-1]
                print("debug ext >> " , ext)
                if ext not in imageType_ext : 
                    continue
               
                test(full_filename, save_path, file_name)

    except PermissionError:
        pass

def main(config) :
    searchfile(config.img_path , config.img_save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CartoonGAN")

    # image path 
    parser.add_argument("--img_path" , type=str, default="./test_img", help= "img_path plze !!")
    
    # image test path 
    parser.add_argument("--img_test_path" , type=str, default="./test_img/5--26.jpg", help= "img_test_path [one image path]")

    # image save path 
    parser.add_argument("--img_save_path" ,type=str, default="./output" , help="img_save_path plz")

    # CartoonGan Model chose 
    parser.add_argument("--model_path" ,type=str, default="./pretrained_model" , help="model_path plz")

    # CartoonGan Style chose 
    parser.add_argument("--CartoonGanStyle" , type=str , default="Hayao_net_G_float.pth" , help="CartoonGanStyle plz")

    config = parser.parse_args()
    main(config)
