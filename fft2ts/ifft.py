import os
from sympy import ifft, fft
import numpy as np
import matplotlib.pyplot as plt

label_dir = "../thought-of-direction/data/mask-iv-openbci/data/left"
dataset = []
for FILE in os.listdir(label_dir):
    ffts = np.load(os.path.join(label_dir, FILE))
    for fft_data in ffts:
        dataset.append(fft_data[:8])


plt.clf()
total_transform = []

for i in range(200):

    sample = dataset[i][0]
    for el in sample:
        total_transform.append(el)


# plt.show()
# # sequence  
# seq = [15, 21, 13, 44]

# # fft 


transform = ifft(total_transform, 4)

tup = map(lambda z: z.as_real_imag(), transform)

x = []
y = []


for z in list(tup):
    x.append(z[0])
    
    y.append(z[1])

pad = len(x)-len(sample)
x = x[pad:-pad]


for el in x:
    total_transform.append(el)


print(len(x))
print("X",x)
print(len(y))
print("Y",y)


# print ("Inverse FFT : ", transform)

print(x)
plt.plot(y)
plt.show()
