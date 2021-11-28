import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import math
import statistics

# Image size
size = 1001
# Gaussian sigma
sigma = 2.5

# Create data for matrix
x = np.arange(0, size, 1, int)
y = x[:, np.newaxis]
# Data in center
x0 = y0 = size // 2

# 2D Gaussian function
g = np.exp(-((x-x0)**2 + (y-y0)**2) / sigma**2)

# Gaussian vector
v = g[x0][:]
# Scale vector
v = (255*(v - np.min(v))/np.ptp(v)).astype(int)
# Show vector
# plt.plot(v)
# plt.show()
# Use vector to create gaussian line across all image
array = np.zeros((size, 1), dtype=v.dtype) + v
# Transform array into image
img = Image.fromarray(np.uint8(array * 255), 'L')
# Rotate
img = img.rotate(6)
# Show image
# img.show()
img.save("img.jpg")

img2 = cv2.imread('img.jpg')
# Find the edges in the image using canny detector
edges = cv2.Canny(img2, 50, 200)
# Detect points that form a line
lines = cv2.HoughLines(edges, 1, np.pi/360, 150)
# Draw lines on the image

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
print(angle)
a_mean = statistics.mean(angle)
print(a_mean)
