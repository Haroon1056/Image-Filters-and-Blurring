# Task 5: Build and Compare Pyramids
# Instructions for the Intern:
# ● Load sample.jpg.
# ● Apply cv2.pyrDown() twice and then cv2.pyrUp() on the result.
# ● Save the images: down1.jpg, down2.jpg, up_from_down2.jpg.
# ● Compare and describe any quality loss during this process.

import cv2

img = cv2.imread("images/sample.jpg")

lower_reso1 = cv2.pyrDown(img)
lower_reso2 = cv2.pyrDown(lower_reso1)
higher_reso = cv2.pyrUp(lower_reso2)

cv2.imshow("Original Image", img)
cv2.imshow("Downsampled 1", lower_reso1)
cv2.imshow("Downsampled 2", lower_reso2)
cv2.imshow("Upsampled", higher_reso)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_images/down1.jpg", lower_reso1)
cv2.imwrite("output_images/down2.jpg", lower_reso2)
cv2.imwrite("output_images/up_from_down2.jpg", higher_reso)


# ● Compare and describe any quality loss during this process.
"""
After applying two rounds of downsampling and then upsampling, I can observe some quality loss in the final image compared to the original. 

When I upsample the second downsampled image (up_from_down2.jpg), the image is enlarged back to the original dimensions, but the lost details cannot be recovered. This results in a blurred and less defined image compared to the original.
"""