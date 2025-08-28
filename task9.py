# Task 9: Object Locator
# Instructions for the Intern:
# ● Take a template image of a logo or small object.
# ● Use cv2.matchTemplate() to find it in a larger scene.
# ● Draw a rectangle around the best match.
# ● Save the result as template_match.jpg.

import cv2

img = cv2.imread("images/sample.jpg")
img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("images/logo.jpg")
template_gry = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

res = cv2.matchTemplate(img_gry, template_gry, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

(h, w) = template_gry.shape[:2]
cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)

cv2.imshow("Template", template)
cv2.imshow("Detected", img)
cv2.imwrite("output_images/template_match.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()