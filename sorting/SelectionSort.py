import random
import time

# Membuat data secara acak
data = [random.randint(0, 100) for a in range (0,random.randint(3,6))]
print ("Data Awal\t:",data)
print()

# Mengambil waktu sekarang untuk dihitung nantinya
start = time.time()

# Menentukan panjang nilainya yang perlu di cek
for b in range (len(data)-1):
    min = b
    # Mencari nilai terkecil
    for c in range (b+1,len(data)):
        if data[min] > data[c]:
            min = c

    # Memindahkan nilai terkecil
    d = data[b]; data[b] = data[min]; data[min] = d
    print('Iterasi ke',(b+1),'\t:',data)

print()
print('Data Akhir\t:',data)

# Mengambil waktu sekarang untuk dihitung
end = time.time()

# Menghitung waktunya dengan cara, waktu yang ada di variabel 'end' dikurangi dengan waktu yang ada di variabel 'start'
print('\nselesai dalam waktu\t:{:f} Detik'.format(end-start))

