import numpy as np
from scipy.ndimage import rotate

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

data = []
for i in range(0, 11):
    # Use vector to create gaussian line across all image
    array = np.zeros((size, 1), dtype=v.dtype) + v
    # Rotate
    angle = i/2
    array = rotate(array, angle)
    array = array[0:1001, 0:1001]
    data.append(array)

np.save("test.npy", data)


