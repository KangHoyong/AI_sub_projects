import json
from pprint import pprint

# test code
# fix add json_train_path 8/19 
def jsonDataReadOneData(json_data, imgRead, json_train_path) : 

    jsonData = [] 
    with open(json_train_path) as f :
        jsonData = json.load(f)

    print("[readJson.py] debug = function : jsonDataRead-> test print code \n" )
    pprint(jsonData[0])

    annotations = jsonData[0]
    fileName = annotations["filename"]
    annos = annotations["ann"]
    bbox = annos["bboxes"]
    labels = annos["labels"]

    return fileName , bbox, labels

def jsonDataRead(json_train_path) :
    
    # json data open code 
    with open(json_train_path) as f :
        jsonData = json.load(f)

    # json file 필요한 Metadata extraction 
    # json file(car_trin.json) -> Name, width, height, bbox , labels Metadata extraction
    # fix code 
    for annotations in jsonData : 
        
        fileName = annotations["filename"]
        print("test code " , fileName)
        width = annotations["width"]
        height = annotations["height"]
    
        annos = annotations["ann"]
        bbox = annos["bboxes"]
        labels = annos["labels"]  

    return fileName, bbox, labels, width, height



