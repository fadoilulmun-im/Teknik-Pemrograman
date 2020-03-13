import random

# Membuat data secara acak
data = [random.randint(0, 100) for a in range (0,random.randint(3,4))]
print ("Data Awal\t:",data)
print()

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

