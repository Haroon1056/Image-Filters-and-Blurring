# Task 4: Apply Geometric Transforms
# Instructions for the Intern:
# ● Take any sample image.
# ● Apply an affine transformation by shifting and rotating a triangle region.
# ● Apply a perspective transformation to simulate a "document scan".
# ● Save results as affine_result.jpg and perspective_result.jpg.

import cv2
import numpy as np

# Affine Transformation
img = cv2.imread("images/document.png")
img = cv2.resize(img, (400, 600))

pts1 = np.float32([[0, 0], [300, 0], [0, 400]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

cv2.imshow("Affine Transform", result)
cv2.imwrite("output_images/affine_result.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Perspective Transformation
img1 = cv2.imread("output_images/affine_result.jpg")

pts1 = np.float32([[12,100], [262, 35], [145, 323], [395, 256]])
pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])

matrix1 = cv2.getPerspectiveTransform(pts1, pts2)
result1 = cv2.warpPerspective(img1, matrix1, (400, 600))

cv2.imshow("Perspective Transform", result1)
cv2.imwrite("output_images/perspective_result.jpg", result1)
cv2.waitKey(0)
cv2.destroyAllWindows()