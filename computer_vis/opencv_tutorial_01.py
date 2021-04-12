import imutils
import cv2


image = cv2.imread("jp.jpg")#reads in input picture
(h,w,d) = image.shape #get h w and depth 
print("width={}. height={}, depth={}".format(w,h,d))

cv2.imshow("Image",image) #open image
cv2.waitKey(0) #waits for a key press to begin again

#acesses pixed at x=50, y=100 
#opencv stores pixel tuple as BGR than RGB
(B,G,R) = image[100,50]
print("R={}, G={}, B={}".format(R,G,B))

#extract a 100x100 pixel square ROI from input image start
#array slicing [startY:endY, StartX:endX]
roi = image [60:160,  320:420]
cv2.imshow("ROI",roi)
cv2.waitKey(0)


