tebakan = [3, 7, 11, 42, 34, 49]
hasil = [5, 9, 11, 42, 3, 49]

benar = 0

for angka in tebakan:
    if angka in hasil:
        benar += 1

print("Jumlah tebakan yang benar:", benar)