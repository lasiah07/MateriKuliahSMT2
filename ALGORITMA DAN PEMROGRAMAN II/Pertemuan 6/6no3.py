jumlah = 0
ganjil = 0
genap = 0

while jumlah < 10:
    angka = int(input("Masukkan angka ke-" + str(jumlah+1) + ": "))

    if angka % 2 == 0:
        genap = genap + 1
    else:
        ganjil = ganjil + 1

    jumlah = jumlah + 1

print("Jumlah angka genap:", genap)
print("Jumlah angka ganjil:", ganjil)