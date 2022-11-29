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



freq, aud_data = scipy.io.wavfile.read('Beatles_corrupt2.wav')
freq2, aud_data2 = scipy.io.wavfile.read('clean_mono.wav')
aud_len = len(aud_data)
#it all begins here, asking the user for an input and create a list out of it
deg_clks = scipy.io.loadmat('degraded_clicks.mat')
deg_lst = list(deg_clks.items())
deg_arr = np.asarray(deg_lst)[3][1][0]
#print(deg_arr)


# converting the inpt degraded clicks dict to array
deg_res = np.where(deg_arr == 1)
deg_res = deg_res[0]
#print(deg_res)

aud_samp = np.zeros(40000)

for i in range(0, 40000):
    aud_samp[i] = aud_data[i]

#print(aud_samp)


plt.subplot(3,1,1)
plt.subplots_adjust(hspace = 1.0)
plt.plot(aud_data2)

plt.title("Clean Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

#plt.show()

plt.subplot(3,1,2)
plt.subplots_adjust(hspace = 1.0)
plt.plot(aud_data)
plt.title("Corrupt Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

#plt.show()

#plt.plot(deg_arr)

#plt.title("Audio Clicks")
#plt.xlabel("No. of Samples")
#plt.ylabel("Amplitude")

#plt.show()

#print(deg_clks)

fltr_lnth = int(input("Enter the length of the filter: "))
#to make sure we input only odd filter length
if fltr_lnth % 2 != 0:
    fltr_lnth = fltr_lnth
else:
    print("Input Error: Number is even")
    fltr_lnth = int(input("Please re-enter the length of the filter: "))

#pad = int((fltr_lnth-1)/2)
#list2 = np.pad(aud_data, (pad,pad), mode='constant', constant_values=(0,0))
#list2 = aud_data

#det = np.where(deg_res==1)
aud_simp = aud_data
#plt.plot(aud_simp)

#plt.title("Audio Input")
#plt.xlabel("No. of Samples")
#plt.ylabel("Amplitude")

#plt.show()

deg_ind = np.arange(len(aud_simp))
#print(len(deg_ind))
deg_y = np.delete(aud_simp, deg_res)
#print(len(deg_y))
deg_h = np.delete(deg_ind, deg_res)
#print(len(deg_h))

aud_data_new = aud_simp
strt_time = time.time()
for i in tqdm(range(100)):
    spline = scipy.interpolate.CubicSpline(deg_h, deg_y, axis=0, bc_type='not-a-knot', extrapolate=None)
    sleep(0.1)
end_time = time.time()
print("Duration: ", (end_time-strt_time))
for i in range (len(deg_res)):
    aud_data_new[deg_res[i]] = spline(deg_res[i])


#print(aud_data_new)
#aud_samp2 = np.zeros(40000)
#for i in range(0, 40000):
    #aud_samp2[i] = aud_data_new[i]

#plt.plot(aud_data_new)
#plt.show()


# fig, axs = plt.subplots(3)
# fig.subplots_adjust(hspace=1.0)
# axs[0].plot(aud_data2)
# axs[0].set_title("Clean Signal")
# axs[1].plot(aud_data)
# axs[1].set_title("Corrupt Signal")
# axs[2].plot(aud_data_new)
# axs[2].set_title("Restored Signal")
# for ax in axs.flat:
#    ax.set(xlabel='No. of Samples', ylabel='Amplitude')
# plt.show()

plt.subplot(3,1,3)
plt.subplots_adjust(hspace = 1.0)

plt.plot(aud_data_new)

plt.title("Restored Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

plt.show()

m1 = aud_data2
m2 = aud_data_new
#mse = np.square(np.subtract(m1,m2)).mean()
#print(mse)
mse = mean_squared_error(m1, m2)
print(mse)
#write("Restored_aud_spline.wav", freq, aud_data_new)

