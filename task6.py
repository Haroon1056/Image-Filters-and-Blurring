# Task 6: Interactive Edge Detector
# Instructions for the Intern:
# ● Use trackbars to control the min and max thresholds of Canny edge detection.
# ● Save a screenshot of your favorite output as tracked_canny.jpg.
# ● Briefly explain how threshold values affect the edge output.

import cv2

img = cv2.imread("images/sample.jpg", 0)

def nothing(x):
    pass

cv2.namedWindow("Canny")
# Create trackbars for thresholds
cv2.createTrackbar("Min", "Canny", 0, 255, nothing)
cv2.createTrackbar("Max", "Canny", 0, 255, nothing)

while True:
    min_val = cv2.getTrackbarPos("Min", "Canny")
    max_val = cv2.getTrackbarPos("Max", "Canny")
    edges = cv2.Canny(img, min_val, max_val)
    cv2.imshow("Canny", edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # ESC key
        cv2.imwrite("output_images/tracked_canny.jpg", edges)
        break

cv2.destroyAllWindows()


# ● Briefly explain how threshold values affect the edge output.
"""
The Canny edge detector uses two threshold values to identify edges in an image. The 'Min' threshold is the lower boundary for edge detection, while the 'Max' threshold is the upper boundary. 
"""