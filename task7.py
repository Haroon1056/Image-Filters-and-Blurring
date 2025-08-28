# Task 7: Histogram Analysis & Enhancement
# Instructions for the Intern:
# ● Load a grayscale image.
# ● Plot and save its histogram using Matplotlib (histogram.png).
# ● Apply cv2.equalizeHist() and CLAHE (adaptive version).
# ● Save enhanced images: equalized.jpg, clahe.jpg.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/img_7.jpg", 0)

# Plot histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.savefig("output_images/histogram.png")
plt.show()

# Equalize
equalized = cv2.equalizeHist(img)

# CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(img)

cv2.imshow("Original", img)
cv2.imshow("Equalized", equalized)
cv2.imshow("CLAHE", clahe_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save enhanced images
cv2.imwrite("output_images/equalized.jpg", equalized)
cv2.imwrite("output_images/clahe.jpg", clahe_img)
