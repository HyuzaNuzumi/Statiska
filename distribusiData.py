import pandas as pd
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

#contoh data:waktu respons server (dalam ms)
data = [120,122,123,121,125,130,300,320,125,127]

#hitung skewness dan kurtosis
sk = skew(data)
#Excesss kurtosis(kurang dari 0 = datar, lebih dari 0 = runcing)
kt = kurtosis(data) 

print("Skewness: ",sk)
print("kurtosis: ",kt)

#visualisasi data
plt.hist(data, bins=8, color = 'skyblue', edgecolor='black')
plt.title('Histogram Waktu Respons Server')
plt.xlabel('Waktu(ms)')
plt.ylabel('Frekuensi')
plt.show()

