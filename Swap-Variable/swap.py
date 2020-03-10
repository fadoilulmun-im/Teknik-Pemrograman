def swap (a,b):
    c = b
    b = a
    a = c
    return(a,b)

awal = input("masukkan nilai awal : ")
akhir = input("masukkan nilai akhir : ")

print("Anda memasukkan nilai awal :",awal)
print("\t\tnilai akhir :",akhir)

awal,akhir = swap (b = akhir,a = awal)

print("Setelah swap : ")
print("\tNilai awal : ",awal,"\n\tNilai akhir : ",akhir)