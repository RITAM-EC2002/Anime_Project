# image processing - making an image blur
import cv2

# Load the image
image = cv2.imread("tiger.jpg")

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# save and display result
cv2.imwrite("tiger_blurred.jpg", blurred)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
