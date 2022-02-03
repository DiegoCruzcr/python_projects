import cv2 
cap = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('q')):
    ret, frame = cap.read()
    cv2.imshow('in live', frame)
    
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


