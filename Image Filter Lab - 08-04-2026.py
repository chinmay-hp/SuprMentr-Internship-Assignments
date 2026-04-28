import cv2

# Load Image (ensure 'image.jpg' is in the same folder)
image = cv2.imread('image.jpg')

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge Detection (Canny)
edges = cv2.Canny(blur, 100, 200)

# Show Images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()