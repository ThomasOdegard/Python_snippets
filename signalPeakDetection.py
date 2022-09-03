
# Finding Maximums/Peaks in Noisy Data

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Generating noisy freq-sweep data.
data = np.sin(2*np.pi*(2**np.linspace(2, 10, 1000))*np.arange(1000) /
              48000) + np.random.normal(0, 1, 1000) * 0.15

fp_distance, _ = find_peaks(data, distance=20)
fp_prominence, _ = find_peaks(data, prominence=1)
fp_width, _ = find_peaks(data, width=20)
# Required vertical distance to its direct neighbouring samples
fp_threshold, _ = find_peaks(data, threshold=0.4)
fp_dist_thresh_width, _ = find_peaks(data, distance=10, threshold=0.2, width=5)

print(f"{fp_distance=}")
print(f"{fp_prominence=}")
print(f"{fp_width=}")
print(f"{fp_threshold=}")
print(f"{fp_dist_thresh_width=}")

# Plotting data.
plt.subplot(3, 2, 1)
plt.title("hard to adjust correct width")
plt.plot(fp_distance, data[fp_distance], "xg")
plt.plot(data)
plt.legend(['distance'])

plt.subplot(3, 2, 2)
plt.title("gives the best solution here")
plt.plot(fp_prominence, data[fp_prominence], "ob")
plt.plot(data)
plt.legend(['prominence'])

plt.subplot(3, 2, 3)
plt.title("track very close peaks is hard")
plt.plot(fp_width, data[fp_width], "vg")
plt.plot(data)
plt.legend(['width'])

plt.subplot(3, 2, 4)
plt.title("only compares with the direct neighbours")
plt.plot(fp_threshold, data[fp_threshold], "xr")
plt.plot(data)
plt.legend(['threshold'])


plt.subplot(3, 2, 5)
plt.title("Combo")
plt.plot(fp_dist_thresh_width, data[fp_dist_thresh_width], "xb")
plt.plot(data)
plt.legend(['dist, threshold and width'])
plt.show()
