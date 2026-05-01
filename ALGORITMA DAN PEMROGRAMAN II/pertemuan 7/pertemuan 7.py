# nomor 1
nilai = [80, 75, 85, 90, 78, 98]
print (nilai[2]) # Ambil nilai ke-3
print (nilai[0:3]) # Ambil 3 nilai pertama
print (nilai[2:]) # Ambil nilai dari index 2 sampai akhir
print (nilai[::2]) # Ambil nilai dengan loncatan(step)

#nomor 2
data_nilai = [
    ["Anandya", 98],
    ["naila", 99],
    ["Anggun", 89],
    ["Sazkia", 78]
]
for siswa in data_nilai:
    print("Nama:", siswa[0], "| Nilai:", siswa[1])

#nomor 3
buah = ["apel", "jeruk", "mangga"]
print(len(buah)) # Len adalah fungsi untuk menghitung jumlah elemen (isi) dalam sebuah list

#nomor 4
buah = ["apel", "jeruk", "mangga"]

del buah[1]
print(buah)

#nomor 5
buah = ["apel", "jeruk", "mangga", "pisang"]
print(buah[-1])
print(buah[-2])
print(buah[-3:])
print(buah[::-1])

#nomor 6
topi_list = [1, 2, 3, 4, 5]

# Langkah 1
topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))

# Langkah 2
del topi_list[-1]

# Langkah 3
print(len(topi_list))

print(topi_list)

#nomor 7
nilai = [10, 20, 30]
print(len(nilai))
print(nilai)
nilai.append(40)
print(len(nilai))
print(nilai)
nilai.insert(1, 15)
print(len(nilai))
print(nilai)

#nomor 8
my_list = [] # membuat list kosong
# mengisi list dengan append yang berulang
for i in range (5):
    my_list.append(i+1)

print(my_list)

#nomor 9
my_list = [] #membuat list kosong

for i in range (5):
    my_list.insert(0, i+1)
print (my_list)

#nomor 10
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#nomor 11
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#nomor 12
my_list = [1, 2, 3, 4, 5]

for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2

print(my_list)

#nomor 13
# Langkah 1: buat list kosong
exo = []
print("Langkah 1:", exo)
# Langkah 2: tambah pakai append
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)
# Langkah 3: tambah pakai for
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in anggota_baru:
    exo.append(anggota)
print("Langkah 3:", exo)
# Langkah 4: hapus anggota
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4:", exo)
# Langkah 5: insert Xiumin di elemen ke-3 dari belakang
exo.insert(len(exo) - 2, "Xiumin")
print("Langkah 5:", exo)
# jumlah anggota
print("Jumlah anggota exo:", len(exo))