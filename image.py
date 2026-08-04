import cv2




img = cv2.imread("resized_khm.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret1, thresh1=cv2.threshold(gray, 127,225,cv2.THRESH_BINARY_INV)
# ret2, thresh2=cv2.threshold(gray, 127,225,cv2.THRESH_BINARY)
cv2.imshow("Thresholded", thresh1)
# cv2.imshow("Thresholded", thresh2)

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

# counters, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

# cv2.drawContours(img, counters, -1, (0, 255, 0), 0)
# print("Number of contours found = " , len(counters))
# print(type(counters))
# print(counters[0])
# print(type(counters[0]))
# print(counters[2].shape)
# cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()