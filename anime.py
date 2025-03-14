import cv2
import numpy as np

# Load the image
image_path = "tiger.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image '{image_path}' not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur
blurred = cv2.medianBlur(gray, 5)


# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth the image
color = cv2.bilateralFilter(image, 9, 255, 250)

# Create cartoon effect
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Convert grayscale images to 3 channels for stacking
gray_colored = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
blurred_colored = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)

# Stack images
top_row = np.hstack((gray_colored, edges_colored))
bottom_row = np.hstack((blurred_colored, cartoon))

# Combine rows
final_image = np.vstack((top_row, bottom_row))

# Show result
cv2.imshow("All Images in One Frame", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
