import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

with open("input1", "r") as f:
    raw_data = [int(line) for line in f.readlines()]
    raw_data.sort()
    data = np.array(raw_data)
    m = np.abs(data[:, None] + data[None, :]-2020)
    mm = np.minimum(m, 1)
    for i, v in enumerate(raw_data):
        print(i, v)
    cm = convolve2d(mm, [
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]])
    plt.imshow(cm)
    plt.colorbar()
    plt.show()