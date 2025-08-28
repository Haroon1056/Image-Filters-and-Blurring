# Task 1: Apply and Compare Filters
# Instructions for the Intern:
# ● Load sample.jpg.
# ● Apply all three filters (Gaussian, Median, Bilateral).
# ● Save each result with filenames: gaussian.jpg, median.jpg, bilateral.jpg.
# ● Write a short note comparing the visual effects of each.

import cv2

# Load the image
img = cv2.imread("images/sample.jpg")

# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(img, (15, 15), 0)

# Apply Median Blur
median = cv2.medianBlur(img, 15)

# Apply Bilateral Filter
bilateral = cv2.bilateralFilter(img, 15, 75, 75)

cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

# Save each result with filenames: gaussian.jpg, median.jpg, bilateral.jpg.
cv2.imwrite("output_images/gaussian.jpg", gaussian)
cv2.imwrite("output_images/median.jpg", median)
cv2.imwrite("output_images/bilateral.jpg", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Write a short note comparing the visual effects of each.
"""
1. Gaussian Blur: This filter smoothens the image by averaging the pixels around a target pixel within a defined kernel size. It is effective in reducing image noise and detail, making it useful for applications like background blurring.

2. Median Blur: This filter replaces each pixel's value with the median value of the intensities in the neighborhood. It is particularly good at removing salt-and-pepper noise while preserving edges better than Gaussian blur.

3. Bilateral Filter: This filter smoothens images while preserving edges by considering both spatial distance and intensity difference. It is more computationally intensive but provides superior results in terms of edge preservation compared to the other two filters.
"""