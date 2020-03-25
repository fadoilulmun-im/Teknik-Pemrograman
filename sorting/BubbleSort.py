import random
import time

# Membuat data secara acak
data = [random.randint(0, 100) for a in range (0,random.randint(3,6))]
print ("Data Awal\t:",data)
print()

# Mengambil waktu sekarang untuk dihitung nantinya
start = time.time()

# Menentukan panjang nilainya yang perlu di cek
for b in range (len(data)):
    
    for c in range (0,len(data)-b-1):
        if data[c] > data[c+1]:

            # Memindahkan datanya jika lebih besar yang awal ke setelahnya
            d = data[c]; data[c] = data[c+1]; data[c+1] = d
        print('Iterasi ke',(b+1,c+1),'\t:',data)

print()
print('Data Akhir\t\t:',data)

# Mengambil waktu sekarang untuk dihitung
end = time.time()

# Menghitung waktunya dengan cara, waktu yang ada di variabel 'end' dikurangi dengan waktu yang ada di variabel 'start'
print('\nselesai dalam waktu\t: {:f} Detik'.format(end-start))
