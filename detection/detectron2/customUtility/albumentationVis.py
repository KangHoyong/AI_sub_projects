# albumentation Visualization Utility code 

import random
import cv2

random.seed(7)

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

BOX_COLOR = (0,255,0) # gren

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
    
    print("debug 1>>" , bboxes)
    print("debug 1-1 >>" , category_ids)

    new_bbox = []
    bbox_number = len(bboxes)
    print("debug 1-2 >> " , bbox_number)
    for i in range(bbox_number):
        x1 = bboxes[i][0]
        y1 = bboxes[i][1]
        x2 = bboxes[i][2]
        y2 = bboxes[i][3]

        new_bbox = x1, y1 ,x2, y2

    print("debug 1-3 >>" , new_bbox)

    for new_bbox, category_id in zip(bboxes, category_ids) : 
        class_name = traget_classes[category_id]
        print("debug 2 >> " ,new_bbox , class_name) 
        # car bbox info show ...
        # if class_name == "Car" : 
        #     # fix code 
        #     print("bbox class_name : Car show .. ")
        #     class_id = class_name
        #     image = visualizeBBox(image, new_bbox, class_id)
        image = visualizeBBox(image, new_bbox, class_name)
    cv2.imshow("windows", image)
    cv2.imwrite("transformsTestImage.png", image)
    if cv2.waitKey(0) & 0xFF == ord("q") : 
        exit()

    # fix save point 
    
    cv2.destroyAllWindows()