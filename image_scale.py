# image processing - making an image grayscale and detects the edges
import cv2
import numpy as np
import os

def load_and_process_image(image_path):
    # Loads an image, converts it to grayscale and applies edge detection
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image is not found!")
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    edges = cv2.Canny(gray, 100, 100) # Apply edge detection

    return gray, edges

def save_image(image, output_path):
    #Saves the processed image to this specified path
    cv2.imwrite(output_path, image)
    print(f"Image saved at {output_path}")

image_path = "tiger.jpg"

# save result
output_gray = "tiger_grayscale_image.jpg"
output_edges = "tiger_edges_detected.jpg"

gray, edges = load_and_process_image(image_path)
if gray is not None and edges is not None:
    save_image(gray, output_gray)
    save_image(edges, output_edges)

# display result
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
