import os
import cv2

# Read Image
image_path = os.path.join('.','imgs','Happy-Guy.jpg')
img = cv2.imread(image_path)
img = cv2.resize(img,(747,498))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img,ksize = (5,5),sigmaX=1,sigmaY=1)


# Draw Contour
ret,thresh = cv2.threshold(gray_img,220,255,cv2.THRESH_BINARY_INV)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cont in contours:
    print(cv2.contourArea(cont))
    if cv2.contourArea(cont) > 2000:
        cv2.drawContours(img,cont,-1,(0,0,255),2,cv2.LINE_AA)
        x1,y1,w,h = cv2.boundingRect(cont)
        cv2.rectangle(img,(x1,y1),(x1 + w, y1 + h),(0,0,255),2)


# Visualize Image
cv2.imshow('Original Image',img)
cv2.imshow('gray_image',gray_img)
cv2.imshow('thresh_image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()