import cv2
import numpy as np

# Save image in set directory 
# Read RGB image 
img = cv2.imread('coin.jpg') 

# Output img with window name as 'image' 
#cv2.imshow('image', img)
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
#channel=int(img.shape[2] * scale_percent /100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 

#cv2.imshow('resized image',resized)
cv2.imwrite('resizedcoins.jpg',resized)
im=cv2.imread('resizedcoins.jpg')
img1 = cv2.medianBlur(im,5)
cimg = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#print('l')
circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    #print('l')
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#cv2.imshow('detected circles',cimg)
cv2.imwrite('circle.jpg',cimg)
ab=cv2.imread('circle.jpg')
if circles is not None:
    circles = np.round(circles[len(circles)-1]).astype("int")
    x = circles
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if (x[i][0]==x[j][0] or abs(x[i][0]-x[j][0])<=10):
            cv2.line(im,(x[i][0],x[i][1]),(x[j][0],x[j][1]),(255,0,0),2)
            #cv2.imshow("lines1",ab)
#ab=cimg.copy()
#cv2.line(im,(0,0),(100,250),(0,0,255),11)
cv2.imshow("lines1",im)
# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)		 

# Destroying present windows on screen 
cv2.destroyAllWindows() 
