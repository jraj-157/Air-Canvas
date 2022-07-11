import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
cv2.namedWindow("test")
 

 
while True:
    img, frame = cap.read()
    if not img:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
 
    if cv2.waitKey(1) == ord('q'):
        break
    
 
cap.release()
 
cv2.destroyAllWindows()
