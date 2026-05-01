#nomor 1
identitas = ("Ciaa", 18, "Cirebon")
print(identitas)

#nomor 2
my_tuple = (1,10,100,1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elemen in my_tuple:
    print (elemen)

#nomor 3
#mengubah tuple menjadi list
data = (1, 2, 3)
temp = list(data)   # ubah ke list
temp[0] = 10        # ubah data
data = tuple(temp)  # balik lagi ke tuple
print(data)  # (10, 2, 3)

#menambahkan elemen(membuat tuple baru)
data = (1, 2, 3)
data = data + (4,)
print(data)  # (1, 2, 3, 4)

#menghapus elemen
data = (1, 2, 3)
temp = list(data)
temp.remove(2)
data = tuple(temp)
print(data)  # (1, 3)

#nomor 4
data = (1, 2, 3)
data2 = (4, 5)

# len()
print("Panjang tuple:", len(data))

# +
gabung = data + data2
print("Gabungan:", gabung)

# *
ulang = data * 2
print("Pengulangan:", ulang)

# in
print("Apakah 2 ada di data?", 2 in data)

# not in
print("Apakah 10 tidak ada di data?", 10 not in data)

#nomor 5
# Penugasan simultan
a, b, c = (1, 2, 3)
print("Nilai a, b, c:", a, b, c)

# Tanpa tanda kurung
x, y = 10, 20
print("Nilai x dan y:", x, y)

# Menukar nilai variabel
m = 5
n = 10
m, n = n, m
print("Hasil setelah ditukar:", m, n)

#nomor 6
# Membuat dictionary
data = {
    "nama": "Ciaa",
    "umur": 18,
    "kota": "Cirebon"
}

# Menampilkan dictionary
print(data)

#nomor 7
data = {
    "nama": "Ciaa",
    "umur": 18,
    "kota": "Cirebon"
}

# Mengakses nilai berdasarkan key
print(data["nama"])
print(data["umur"])

# Menggunakan get()
print(data.get("kota"))

#nomor 8
data = {
    "nama": "Ciaa",
    "umur": 18,
    "kota": "Cirebon"
}

# Mengambil semua key
kunci = data.keys()

print(kunci)

#nomor 9
data = {
    "nama": "Ciaa",
    "umur": 18,
    "kota": "Cirebon"
}

# Mengambil semua nilai
nilai = data.values()

print(nilai)

#nomor 10
data = {
    "nama": "Ciaa",
    "umur": 18,
    "kota": "Cirebon"
}

# Mengambil semua key dan value
item = data.items()

print(item)

#nomor 11
data = {
    "nama": "Ciaa",
    "umur": 18
}

# Menambahkan data baru
data.update({"kota": "Cirebon"})

# Mengubah data yang sudah ada
data.update({"umur": 19})

print(data)

#nomor 12
data = {
    "nama": "Ciaa",
    "umur": 18,
    "kota": "Cirebon"
}

# Menghapus item terakhir
hasil = data.popitem()

print("Data yang dihapus:", hasil)
print("Sisa data:", data)

#nomor 13
data = {
    "nama": "Ciaa",
    "umur": 18
}

# Mengubah nilai
data["umur"] = 19

# Menambahkan data baru
data["kota"] = "Cirebon"

# Menghapus data
del data["nama"]

print(data)

#nomor 14
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")

else:
    print("Program berjalan tanpa error")

finally:
    print("Program selesai")

#nomor 15
try:
    saldo = 100000  # saldo awal
    ambil = int(input("Masukkan jumlah uang yang ingin diambil: "))

    hasil = saldo - ambil

    if ambil <= 0:
        raise ValueError("Jumlah harus lebih dari 0")
    elif ambil > saldo:
        raise Exception("Saldo tidak cukup")

    print("Uang berhasil diambil")
    print("Sisa saldo:", hasil)

except ValueError:
    print("Error: input harus berupa angka dan tidak boleh nol/negatif")

except Exception as e:
    print("Error:", e)