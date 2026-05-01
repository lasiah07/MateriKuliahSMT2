a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if a > b:
    print("Angka pertama lebih besar")
    print("Selisihnya:", a - b)
elif a < b:
    print("Angka kedua lebih besar")
    print("Selisihnya:", b - a)
else:
    print("Kedua angka sama")