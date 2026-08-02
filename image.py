import cv2

img = cv2.imread("resized_khm.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (9,9),0)

cv2.imshow("Gray", gray)
cv2.imshow("Blurred", blr)


cv2.waitKey(0)
cv2.destroyAllWindows()