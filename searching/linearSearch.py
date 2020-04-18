def linierSearch(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return False


arr = [1, 3, 10, 90, 8, 9]
x = 7
hasil = linierSearch(arr, len(arr), x)
if hasil:
    print("Elemen di temukan di index ke", hasil)
else:
    print("Elemen yang dicari tidak ada dalam array")
