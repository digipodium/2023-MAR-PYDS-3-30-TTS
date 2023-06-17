import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\LENOVO\Documents\PyDS\XlO9.gif')

#if the camera is open or not
if (cap.isOpened()==False):
    print("Error opening video stream or file")

#Read the entire file until it is completed
while(cap.isOpened()):
    #capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        #display the resulting frame
        cv2.imshow('Frame',frame)
        #press Q on keyboard to exit
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    #break the loop
    else:
        break

#When everything done, release the video capture object
cap.release()

#Closes all the frames
cv2.destroyAllWindows()
