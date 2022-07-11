import cv2
 
cap = cv2.VideoCapture(0)
 
cv2.namedWindow("test")
 
img_counter = 0
 
while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
 
    k = cv2.waitKey(1)
    
 
cap.release()
 
cv2.destroyAllWindows()