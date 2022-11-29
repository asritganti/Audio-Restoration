from median import median_fltr
import numpy as np
import scipy as sc
import scipy.io
import scipy.io.wavfile
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from time import sleep
import time
from tqdm import tqdm
from sklearn.metrics import mean_squared_error

# it all begins here, asking the user for an input and create a list out of it
freq, aud_data = scipy.io.wavfile.read('Beatles_corrupt2.wav')
freq2, aud_data2 = scipy.io.wavfile.read('clean_mono.wav')
aud_len = len(aud_data)

deg_clks = scipy.io.loadmat('degraded_clicks.mat')
deg_lst = list(deg_clks.items())
deg_arr = np.asarray(deg_lst)[3][1][0]
# print(deg_arr)


# converting the inpt degraded clicks dict to array
deg_res = np.where(deg_arr == 1)
deg_res = deg_res[0]
# print(deg_res)

plt.subplot(3, 1, 1)
plt.subplots_adjust(hspace=1.0)
plt.plot(aud_data2)

plt.title("Clean Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")


plt.subplot(3, 1, 2)
plt.subplots_adjust(hspace=1.0)
plt.plot(aud_data)
plt.title("Corrupt Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

aud_simp = aud_data
#Creating arrays without the values with the clicks
deg_ind = np.arange(len(aud_simp))
# print(len(deg_ind))
deg_y = np.delete(aud_simp, deg_res)
# print(len(deg_y))
deg_h = np.delete(deg_ind, deg_res)
# print(len(deg_h))

aud_data_new = aud_simp
# running the cubic spline interpolation funtion
strt_time = time.time()
for i in tqdm(range(100)):
    spline = scipy.interpolate.CubicSpline(
        deg_h, deg_y, axis=0, bc_type='not-a-knot', extrapolate=None)
    sleep(0.1)
end_time = time.time()
print("Duration: ", (end_time-strt_time))
for i in range(len(deg_res)):
    aud_data_new[deg_res[i]] = spline(deg_res[i])
# plotting the restored signal
plt.subplot(3, 1, 3)
plt.subplots_adjust(hspace=1.0)

plt.plot(aud_data_new)

plt.title("Restored Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

plt.show()

# Calculating the MSE
m1 = aud_data2
m2 = aud_data_new
#mse = np.square(np.subtract(m1,m2)).mean()
# print(mse)
mse = mean_squared_error(m1, m2)
print("Mean-Squared Error", mse)
#creating the restored audio file in wav
#write("Restored_aud_spline.wav", freq, aud_data_new)
print("Done, yay?")
