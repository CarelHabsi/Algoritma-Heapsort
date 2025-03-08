# Carel Habsian Osagi (23343061), Informatika
# Heapsort

# Fungsi untuk membentuk Max-Heap
def susun_heap(data, ukuran_heap, indeks):
    terbesar = indeks  
    kiri = 2 * indeks + 1   
    kanan = 2 * indeks + 2  

    if kiri < ukuran_heap and data[kiri] > data[terbesar]:
        terbesar = kiri
    if kanan < ukuran_heap and data[kanan] > data[terbesar]:
        terbesar = kanan
    if terbesar != indeks:
        data[indeks], data[terbesar] = data[terbesar], data[indeks]  
        susun_heap(data, ukuran_heap, terbesar)  

# Fungsi Heapsort
def heapsort(data):
    ukuran_data = len(data)

    # Bangun max heap
    for i in range(ukuran_data // 2 - 1, -1, -1):
        susun_heap(data, ukuran_data, i)

    # Pengurutan dengan menukar elemen terbesar ke akhir
    for i in range(ukuran_data - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  
        susun_heap(data, i, 0)  

# Contoh penggunaan
data = [12, 11, 13, 5, 6, 7, 9, 10, 8, 15, 14, 4]
print("Data sebelum diurutkan:", data)
heapsort(data)
print("Data setelah diurutkan:", data)