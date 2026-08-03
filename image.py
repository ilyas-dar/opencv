import cv2




img = cv2.imread("resized_khm.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret, thresh=cv2.threshold(gray, 127,225,cv2.THRESH_BINARY)
bret, thresht=cv2.threshold(img, 127,225,cv2.THRESH_BINARY)
print(ret)
print(bret)
cv2.imshow("Threshold", thresh)
cv2.imshow("Thresholdd", thresht)
# blr = cv2.GaussianBlur(img, (5,5),0)

# cv2.imshow("Original", img)
# edge=cv2.Canny(img, 100, 200)
# cv2.imshow("Edges", edge )


# cv2.imshow("Gray", gray)
# cv2.imshow("Blurred", blr)


# blue=img[:,:,0]
# green=img[:,:,1]
# red=img[:,:,2]



# blue_img = img.copy()
# blue_img[:,:,1] = 0
# blue_img[:,:,2] = 0
# cv2.imshow("Blue Channel", blue)
# cv2.imshow("Green Channel", green)
# cv2.imshow("Red Channel", red)
# cv2.imshow("Blue Image", blue_img)

# print(img[0,0])
# print(blue[0,0])
# print(green[0,0])
# print(red[0,0]) .



cv2.waitKey(0)
cv2.destroyAllWindows()