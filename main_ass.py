from median import median_fltr
import numpy as np
import scipy as sc
import scipy.io
import scipy.io.wavfile 
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy import signal
from playsound import playsound





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
print(deg_res)

#list1 = []

plt.plot(aud_data)

plt.title("Audio Input")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

plt.show()

print(deg_clks)

#n = int(input("Enter the number of elements: "))
#for i in range(0, n):
    #box = int(input())
    #list1.append(box)

#print(list1)

fltr_lnth = int(input("Enter the length of the filter: "))
#to make sure we input only odd filter length
if fltr_lnth % 2 != 0:
    fltr_lnth = fltr_lnth
else:
    print("Input Error: Number is even")
    fltr_lnth = int(input("Please re-enter the length of the filter: "))

pad = int((fltr_lnth-1)/2)
#list2 = np.pad(aud_data, (pad,pad), mode='constant', constant_values=(0,0))
list2 = aud_data

#life gets tough but we got code
#for loop to filter the elements and adding them to a new list
list3 = list2


for i in range (0,len(deg_res)):
    rem = deg_res[i]
    temp_lst = []
    for j in range (rem, (rem+fltr_lnth)):
        temp_lst.append(list2[j])
    temp_med = median_fltr(temp_lst)
    print(temp_lst)
    print(temp_med)
    list3[rem] = temp_med

print(list3)

plt.plot(list3)

plt.title("Audio Input")
plt.xlabel("No. of Samples")
plt.ylabel("Amplitude")

plt.show()
write("Restored_aud.wav", freq, list3)

m1 = aud_data2
m2 = list3
mse = np.square(np.subtract(m1,m2)).mean()
print(mse)

#playsound('Restored_aud.wav')


#stay chill yo, we using the inbuilt function for the filter
#list4 = signal.medfilt(aud_data, kernel_size=3)
#print(list4)
#checking the output
#check = np.array_equal(list3, list4)
#print(check)

