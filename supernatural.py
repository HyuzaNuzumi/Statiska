def hitungMean(data):
    total =sum(data)
    jumlah_data = len(data)
    mean = total / jumlah_data
    return mean

def hitungMedian(data):
    data_urut = sorted(data)
    jumlah_data = len(data_urut)

    #jika jumlah data ganjil, ambil nilai tengah
    if jumlah_data % 2 == 1:
        median = data_urut[jumlah_data // 2]
    #jika jumlah data genap, ambil rata-rata dua nilai tengah
    else:
        tengah_kiri = data_urut [(jumlah_data // 2) - 1]
        tengah_kanan = data_urut [jumlah_data // 2]
        median = (tengah_kiri + tengah_kanan) / 2

        return median
    
def hitungModus(data):
    #Hitung frekuensi setiap angka dalam data
    frekuensi = [0] * (max(data) + 1) #Buat list dengan ukuran maksimum angka dalam data +1

    for angka in data:
        frekuensi[angka] += 1

    #cari frekuensi tertinggi
    frekuensi_tertinggi = max(frekuensi)

    #cari angka-angka dengan frekuensi tertinggi(modus)
    modus = []
    for angka in data:
        if frekuensi[angka] == frekuensi_tertinggi and angka not in modus:
            modus.append(angka)

    return modus

def main():
    #Data
    data = [200,182,199,24,92,90,101,92,16,152,92,82,77,72,92,81]

    mean = hitungMean(data)
    median = hitungMedian(data)
    modus = hitungModus(data)

    print("Mean dari data adalah: ", mean)
    print("Median dari data adalah: ", median)

    if len(modus) == 1:
        print("Modus: ", modus[0])
    else:
        print("Data memiliki beberapa Modus: ", modus)

main()