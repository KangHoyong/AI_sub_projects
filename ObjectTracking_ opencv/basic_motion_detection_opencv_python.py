import cv2

cap = cv2.VideoCapture("ObjectTracking_code/videoDataset/vtest.avi")

ret , frame1 = cap.read()
ret , frame2 = cap.read()


while cap.isOpened() : 
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # contours 
    befor_frame1 = frame1.copy()

    for contour in contours : 
        (x, y , w , h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900 : 
            continue
        #  박스 그려주기 contours (x,y,x1,y1)
        cv2.rectangle(frame1, (x , y) , (x+w , y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status : {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1 ,(0,0,255),3)

    befor_frame2 = cv2.drawContours(befor_frame1, contours, -1, (0,255,0), 2)
    
    cv2.imshow("beforTest", befor_frame2)
    cv2.imshow("windows", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    
    keyboard = cv2.waitKey(30) 
    if keyboard == 27 : 
        break

cap.release()
cv2.destroyAllWindows()