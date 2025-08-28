# Mini Project: Shape Counter
# Project Objective:
# Count the number of geometric shapes (circles, squares, triangles) in an image using contours
# and classification logic.
# Hints:
# ● Use cv2.findContours()
# ● Use cv2.approxPolyDP() to classify based on number of sides
# ● Use cv2.putText() to label each shape
# Final Task: Shape Counter App
# Instructions for the Intern:
# ● Create shape_counter.py
# ● Load a shape-rich image (circles, rectangles, etc.)
# ● Detect and label each shape (Triangle, Square, Circle, etc.)
# ● Print the count of each shape.
# ● Save the final annotated image as shapes_detected.jpg


import cv2
import numpy as np

# Load image
img = cv2.imread('images/shape.jpg')
img = cv2.resize(img, (600, 400))

# Convert to grayscale and threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Shape counter
shape_count = {"Triangle": 0, "Square": 0, "Rectangle": 0, "Circle": 0,
               "Pentagon": 0, "Hexagon": 0, "Star": 0, "Other": 0}

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    shape_type = "Other"

    if len(approx) == 3:
        shape_type = "Triangle"
        shape_count["Triangle"] += 1
    elif len(approx) == 4:
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_type = "Square"
            shape_count["Square"] += 1
        else:
            shape_type = "Rectangle"
            shape_count["Rectangle"] += 1
    elif len(approx) == 5:
        shape_type = "Pentagon"
        shape_count["Pentagon"] += 1
    elif len(approx) == 6:
        shape_type = "Hexagon"
        shape_count["Hexagon"] += 1
    else:
        # Check for circle using circularity
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter != 0:
            circularity = 4 * np.pi * (area / (perimeter * perimeter))
            if 0.7 <= circularity <= 1.2:
                shape_type = "Circle"
                shape_count["Circle"] += 1
            elif 8 <= len(approx) <= 12:  # rough star detection
                shape_type = "Star"
                shape_count["Star"] += 1
            else:
                shape_count["Other"] += 1

    # Draw and label
    cv2.putText(img, shape_type, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

# Print counts
print("Shape counts:")
for shape, count in shape_count.items():
    if count > 0:
        print(f"{shape}: {count}")

# Show output
cv2.imshow("Shape_Detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save result
cv2.imwrite("output_images/shapes_detected.jpg", img)
