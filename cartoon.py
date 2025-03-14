# image processing - making an image cartoonized
import cv2
import numpy as np

# Load an image
image = cv2.imread("tiger.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur
blurred = cv2.medianBlur(gray, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth the image
color = cv2.bilateralFilter(image, 9, 255, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# save and display result
cv2.imwrite("tiger_cartoon.jpg", cartoon)
cv2.imshow("Cartoon Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
