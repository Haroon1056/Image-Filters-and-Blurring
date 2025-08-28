# Task 3: Blend and Mask
# Instructions for the Intern:
# ● Blend two images together using cv2.addWeighted.
# ● Create a mask with a rectangle or circle.
# ● Apply a bitwise AND operation to show only the masked region.
# ● Save the output as blended.jpg and masked.jpg.

import cv2
import numpy as np

img1 = cv2.imread("images/sample.jpg")
img2 = cv2.imread("images/img_7.jpg")

# Resize img2 to match img1
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Create a mask
mask = np.zeros(img1.shape[:2], dtype="uint8")
cv2.rectangle(mask, (300, 20), (400, 150), 255, -1)

# Apply the mask
masked = cv2.bitwise_and(blended, blended, mask=mask)

# Display the outputs
cv2.imshow("Blended Image", blended)
cv2.imshow("Masked Region", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the outputs
cv2.imwrite("output_images/blended.jpg", blended)
cv2.imwrite("output_images/masked.jpg", masked)