import json
import cv2

# test code 
def drawBBoxOneImageTest(img, fileName, bbox , labels, tragetClasses) :
    print("[drawBBox.py] debug = function : drawBBoxOneImageTest -> test print code : \n")
    print(fileName, "\n" , bbox, "\n" ,labels)
    
    bboxNumber = len(bbox)
    print("[drawBBox.py] debug = function : drawBBoxOneImageTest -> test print code : " , bboxNumber)
    
    for index in range(bboxNumber) : 
        x1 = bbox[index][0]
        y1 = bbox[index][1]
        x2 = bbox[index][2]
        y2 = bbox[index][3]

        print("[drawBBox.py] debug x1, y1 , x2, y2" , x1, y1, x2, y2)
        labelsNumber = labels[index]
        print("[drawBBox.py] debug labelsNumber " , labelsNumber )

        # draw bbox and labels one image test code 
        p1 = x1
        p2 = y1 - 10 
        print("Test" , p1, p2)
        id= tragetClasses[labelsNumber]
        
        i img = cv2.putText(img, id, (p1, p2), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,255,0), 2)

    cv2.imshow("windows" , img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        exit()mg = cv2.rectangle(img, (x1, y1) , (x2, y2) , (0,255,0), 3)
       


