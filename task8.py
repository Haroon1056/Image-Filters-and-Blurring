# Task 8: Morphological Processing
# Instructions for the Intern:
# ● Use a binary image with noise.
# ● Apply erosion, dilation, opening, and closing.
# ● Save results: erosion.jpg, dilation.jpg, opening.jpg, closing.jpg.
# ● Briefly explain the differences.

import cv2
import numpy as np

img = cv2.imread("images/binary.jpg", 0)
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


cv2.imshow("Original", img)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_images/erosion.jpg", erosion)
cv2.imwrite("output_images/dilation.jpg", dilation)
cv2.imwrite("output_images/opening.jpg", opening)
cv2.imwrite("output_images/closing.jpg", closing)

# ● Briefly explain the differences.
"""
Erosion removes small-scale noise by eroding away the boundaries of foreground objects.
Dilation adds pixels to the boundaries of objects, effectively increasing their size.
Opening is an erosion followed by dilation, useful for removing small objects from the foreground.
Closing is a dilation followed by erosion, useful for closing small holes in the foreground.
"""