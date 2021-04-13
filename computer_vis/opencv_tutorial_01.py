#import imutils
#from cv_util_func import *
#below code imports entire file 
import cv_util_func as cv_util
import cv2

#use 0 for new_var if not specified
#def aspect_ratio(w,h,new_width,new_height):

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

resized = cv2.resize(image, (200,200))
cv2.imshow("Fixed Resizing",resized)
cv2.waitKey(0)

#compute new hieight based on aspect ratio new width is gonna be 
#300px
#aspect ratio formula take new width / old width
#times that by the height
"""
r = 300.0 /w
dim = (300,int(h*r))
"""
print (w,h)
resized_tuple =cv_util.aspect_ratio(w,h,300,0)
print(resized_tuple)
#resized = cv2.resize(image,dim)
resized = cv2.resize(image,resized_tuple)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)




