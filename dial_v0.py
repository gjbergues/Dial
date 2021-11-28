import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import math
import statistics


def angle(i):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        a0 = abs(math.degrees(math.atan2(y2 - y1, x2 - x1)))
    return a0


# Read Image
img = cv2.imread('img/1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# show the original and blurred images
# cv2.imshow("Blurred", blurred)

# compute a "wide", "mid-range", and "tight" threshold for the edges
# using the Canny edge detector
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)
# show the output Canny edge maps
# cv2.imshow("Wide Edge Map", wide)
# cv2.imshow("Mid Edge Map", mid)   
# cv2.imshow("Tight Edge Map", tight)
# cv2.waitKey(10000)

# Find the edges in the image using canny detector
# edges = cv2.Canny(img, 50, 200)
# Detect points that form a line
lines = cv2.HoughLines(tight, 1, np.pi/360, 150)

a1 = angle(0)
a2 = angle(1)
A = (a1-a2)/2 + a2
print(A)

# scale measurement
# 1 dic = 3.6º
m = A/3.6
print(m)

cv2.imwrite('result/hough.jpg', img)
