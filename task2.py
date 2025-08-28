# Task 2: Create Your Own Filters
# Instructions for the Intern:
# ● Load an image and apply both the sharpening and edge detection kernels.
# ● Try changing values in the kernel to create a custom effect.
# ● Save the outputs: sharpened.jpg, edges.jpg, custom_filter.jpg.
# ● Write 2-3 lines describing the effect of the custom filter

import cv2
import numpy as np

img = cv2.imread("images/sample.jpg")

# Sharpening kernel
kernel_sharpen = np.array([[0, -1, 0],
                            [-1, 5,-1],
                            [0, -1, 0]])

# Edge Detection Kernel
kernel_edge = np.array([[-1, -1, -1],
                         [-1,  8, -1],
                         [-1, -1, -1]])

# Custom Filter
kernel_custom = np.array([[1, 1, 1],
                           [1, -7, 1],
                           [1, 1, 1]])


sharpened = cv2.filter2D(img, -1, kernel_sharpen)
edges = cv2.filter2D(img, -1, kernel_edge)
custom_filter = cv2.filter2D(img, -1, kernel_custom)

cv2.imshow("Sharpened Image", sharpened)
cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Custom Filter Image", custom_filter)
cv2.imshow("Original Image", img)

# Save the outputs: sharpened.jpg, edges.jpg, custom_filter.jpg.

cv2.imwrite("output_images/sharpened.jpg", sharpened)
cv2.imwrite("output_images/edges.jpg", edges)
cv2.imwrite("output_images/custom_filter.jpg", custom_filter)


cv2.waitKey(0)
cv2.destroyAllWindows()

# Write 2-3 lines describing the effect of the custom filter

""" The custom filter enhances the edges while maintaining the overall brightness of the image. It effectively highlights the contours and details, making it useful for applications requiring edge detection without losing important visual information. """