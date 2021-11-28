import numpy as np
from PIL import Image
import cv2
import math
import statistics

data = np.load("test.npy")
# Transform array into image
img = Image.fromarray(np.uint8(data[3] * 255), 'L')
img.show()
img.save("img.jpg")
# Read Image
img2 = cv2.imread('img.jpg')

# Find the edges in the image using canny detector
edges = cv2.Canny(img2, 50, 200)
# Detect points that form a line
lines = cv2.HoughLines(edges, 1, np.pi/360, 150)

angle = []
for i in lines:
    rho = i[0][0]
    theta = i[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img2, (x1, y1), (x2, y2), (0, 0, 255), 2)
    c = math.degrees(math.atan2(y2-y1, x2-x1))
    angle.append(abs(c))
print(angle[0:4])
a_mean = statistics.mean(angle[0:4])
print(180-a_mean)
