import math

n = int (input("\nBanyak Data: "))
data = []
jumlah = 0 
for i in range(n):
    temp =  int (input("Masukkan data ke-%d: " %(i+1)))
    data.append (temp) 
    jumlah += data[i]
    rata = (jumlah / n )

jum = 0
for i in range(n):
    jumlah = jumlah + (data[i]- rata)**2
    deviasi = math.sqrt(jumlah/(n-1))

print ("Data yang di masukkan (%d data) adalah: " %(n), list(data))
print ("\nHasil Nilai Rata-rata = %0.2f" % rata)
print ("Nilai standar Deviasi adalah = ", deviasi)