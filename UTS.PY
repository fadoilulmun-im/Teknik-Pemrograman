from time import time
from re import match
from random import randint


def Input():
    global pilihan, data
    while pilihan != 4:
        print("\nPisahkan hanya dengan Spasi!")
        print("Silahkan dikosongi untuk data acak")
        data = input("Masukkan data angka\t: ")
        if data == "":
            data = [randint(0, 100) for a in range(0, randint(3, 6))]
            menu()
        elif data != "":
            if match(r"(?=\d+)[\d\s]+$", data):
                data = data.split()
                menu()
            else:
                print(
                    "\033[91m {}\033[00m".format(
                        "\ndata hanya bisa berisi angka, dan dipisah hanya dengan Spasi !"
                    )
                )


def menu():
    global pilihan
    while pilihan != 4:
        print("\nData awal\t:", data)
        print("\nPilih Menu\n")
        print("1. Selecton Sort")
        print("2. Bubble Sort")
        print("3. Ubah data")
        print("4. Keluar")
        pilihan = input("Masukkan nomor pilihan disini\t: ")
        print()
        if pilihan.isnumeric():
            pilihan = int(pilihan)
            if pilihan == 1:
                print("Data awal\t:", data)
                print()
                Selection()
            elif pilihan == 2:
                print("Data awal\t\t:", data)
                print()
                Bubble()
            elif pilihan == 3:
                Input()
            elif (pilihan < 1) or (pilihan > 4):
                print("\033[91m{} {} {}\033[00m".format("Tidak ada pilihan No", pilihan, '!'))
        else:
            print("\033[91m{}\033[00m".format("Pilihan harus angka !"))


def Selection():
    start = time()
    for b in range(len(data) - 1):
        min = b
        for c in range(b + 1, len(data)):
            if int(data[min]) > int(data[c]):
                min = c
        d = data[b]
        data[b] = data[min]
        data[min] = d
        print("Iterasi ke", (b + 1), "\t:", data)

    print()
    print("Data Akhir\t:", data)
    end = time()
    print("\nselesai dalam waktu\t:{} Detik".format(end - start))


def Bubble():
    start = time()
    for b in range(len(data)):
        for c in range(0, len(data) - b - 1):
            if int(data[c]) > int(data[c + 1]):
                d = data[c]
                data[c] = data[c + 1]
                data[c + 1] = d
            print("Iterasi ke", (b + 1, c + 1), "\t:", data)
    print()
    print("Data Akhir\t\t:", data)
    end = time()
    print("\nselesai dalam waktu\t: {} Detik".format(end - start))
    print("-" * 55)


print("-" * 28)
print("Nama\t: Fadoilul Mun'im\nNIM\t: 04319017")
print("-" * 28)

pilihan = 0

Input()
