from median import median_fltr
import numpy as np
import scipy as sc
import scipy.io
import scipy.io.wavfile
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy import signal
from time import sleep
import time
from tqdm import tqdm
import unittest
from sklearn.metrics import mean_squared_error


freq, aud_data = scipy.io.wavfile.read('Beatles_corrupt2.wav')
freq2, aud_data2 = scipy.io.wavfile.read('clean_mono.wav')
aud_len = len(aud_data)
# it all begins here, asking the user for an input and create a list out of it
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
plt.plot(aud_data)

plt.title("Clean Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.subplots_adjust(hspace=1.0)
plt.plot(aud_data)

plt.title("Degraded Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")


fltr_lnth = int(input("Enter the length of the filter: "))
# to make sure we input only odd filter length
if fltr_lnth % 2 != 0:
    fltr_lnth = fltr_lnth
else:
    print("Input Error: Number is even")
    fltr_lnth = int(input("Please re-enter the length of the filter: "))

#pad = int((fltr_lnth-1)/2)
#list2 = np.pad(aud_data, (pad,pad), mode='constant', constant_values=(0,0))
list2 = aud_data

# life gets tough but we got code
# for loop to filter the elements and adding them to a new list
list3 = list2

strt_time = time.time()
for k in tqdm(range(100)):
    for i in range(0, len(deg_res)):
        rem = deg_res[i]
        temp_lst = []
        for j in range(rem, (rem+fltr_lnth)):
            temp_lst.append(list2[j])
        temp_med = median_fltr(temp_lst)
        # print(temp_lst)
        # print(temp_med)
        list3[rem] = temp_med
    sleep(0.07)
end_time = time.time()
print("Duration: ", (end_time-strt_time))
# print(list3)


plt.subplot(3, 1, 3)
plt.subplots_adjust(hspace=1.0)
plt.plot(list3)

plt.title("Restored Signal")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")
plt.show()
#write("Restored_aud.wav", freq, list3)

m1 = aud_data2
m2 = list3
#mse = np.square(np.subtract(m2,m1)).mean()
# print(mse)
mse = abs(mean_squared_error(m1, m2))
print("Mean Squared Error", mse)

list4 = list2


class testing_mthds(unittest.TestCase):
    def test_mdnfltr(self):
        for i in range(0, len(deg_res)):
            rem = deg_res[i]
            temp_lst = []
            for j in range(rem, (rem+fltr_lnth)):
                temp_lst.append(list2[j])
            temp_med = scipy.signal.medfilt(temp_lst, kernel_size=fltr_lnth)
            # print(temp_lst)
            # print(temp_med)
            gj = int((fltr_lnth-1)/2)
        list4[rem] = temp_med[gj]
        akjs = np.array_equal(list4, list3)


print("Done, yay?")
unittest.main()
