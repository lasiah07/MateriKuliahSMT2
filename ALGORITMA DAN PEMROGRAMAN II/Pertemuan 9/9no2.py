angka = [3, 1, 2]

print("Awal:", angka)

for i in range(len(angka)):
    for j in range(len(angka)-1):
        if angka[j] > angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]
        print(angka)

print("Akhir:", angka)