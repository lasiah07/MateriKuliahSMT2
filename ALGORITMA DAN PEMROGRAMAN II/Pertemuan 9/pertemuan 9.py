#nomor 1
botol = [20, 15, 25, 10]

for i in range(len(botol)):
    for j in range(len(botol)-1):
        if botol[j] > botol[j+1]:
            # tukar posisi
            botol[j], botol[j+1] = botol[j+1], botol[j]

print("Urutan botol:", botol)

#nomor 2
angka = [3, 1, 2]

print("Awal:", angka)

for i in range(len(angka)):
    for j in range(len(angka)-1):
        if angka[j] > angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]
        print(angka)

print("Akhir:", angka)

#nomor 3
nilai = [80, 60, 90, 70]

nilai.sort()

print(nilai)

#nomor 4
data = [3, 1, 2]

data.reverse()
print(data)

#nomor 5
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print (list_2)

#nomor 6
data = [10, 20, 30, 40, 50]

print("Data asli:", data)

print("Slice [1:4]:", data[1:4])   # ambil tengah
print("Slice [:3]:", data[:3])     # dari awal
print("Slice [2:]:", data[2:])     # sampai akhir
print("Slice [:]:", data[:])       # semua

#nomor 7
data = [10, 20, 30, 40, 50]
#        0   1   2   3   4
#       -5  -4  -3  -2  -1
print(data[1:-1])

#nomor 8
data = [10, 20, 30, 40, 50]
#        0   1   2   3   4
#       -5  -4  -3  -2  -1
print(data[-4:3])

#nomor 9
data = [10, 20, 30, 40, 50]
#        0   1   2   3   4
print(data[:3])

#nomor 10
data = [10, 20, 30, 40, 50]
#        0   1   2   3   4
print(data[2:])

#nomor 11
data = [10, 20, 30, 40, 50]

print(data[:])

#nomor 12
data = [10, 20, 30, 40, 50]

del data[1:4]

print(data)

#nomor 13
data = [10, 20, 30]

del data [:]

print(data)

#nommor 14
data = [10, 20, 30]

del data

#nomor 15
angka = [10, 20, 30]

print(20 in angka)
print(5 in angka)

#nomor 16
angka = [10, 20, 30]

print(5 not in angka)

#nomor 17
my_list = [17,3,11,5,1,9,7,15,13]
largest = my_list [0]

for i in range (1, len(my_list)):
    if my_list[i] > largest :
        largest = my_list[i]

print(largest)

#nomor 18
my_list = [17,3,11,5,1,9,7,15,13]
largest = my_list [0]

for i in range (1, len(my_list)):
    if my_list[i] > largest :
        largest = my_list[i]

print(largest)

#nomor 19
my_list = [1,2,3,4,5,6,7,8,9,10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list [i] == to_find
    if found :
        break

if found :
    print("Elemen ditemukan pada index ke-", i)
else :
    print("Tidak ada di dalam list")

#nomor 20
tebakan = [3, 7, 11, 42, 34, 49]
hasil = [5, 9, 11, 42, 3, 49]

benar = 0

for angka in tebakan:
    if angka in hasil:
        benar += 1

print("Jumlah tebakan yang benar:", benar)

#nomor 21
data = [
    ["Nama", "Usia", "Kota"],
    ["Andi", 20, "Jakarta"],
    ["Budi", 22, "Bandung"],
    ["Citra", 19, "Surabaya"]
]

for baris in data:
    for kolom in baris:
        print(kolom, end=" | ")
    print()