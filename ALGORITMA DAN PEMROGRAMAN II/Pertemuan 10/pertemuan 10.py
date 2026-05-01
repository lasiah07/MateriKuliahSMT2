#nomor 1
baris = ["pion_putih" for i in range (8)]
print(baris)

pion_putih = "♙"
baris = [pion_putih for i in range(8)]
print(baris)

#nomor 2
# Simbol
KOSONG = "."
Benteng = "♜"
Kuda = "♞"
# Membuat papan catur 8x8
papan_catur = []
for i in range(8):
    baris = [KOSONG for j in range(8)]
    papan_catur.append(baris)
# Mengisi Benteng (pojok)
papan_catur[0][0] = Benteng
papan_catur[0][7] = Benteng
papan_catur[7][0] = Benteng
papan_catur[7][7] = Benteng
# Mengisi Kuda (contoh posisi)
papan_catur[4][2] = Kuda
# Menampilkan papan
for baris in papan_catur:
    print(baris)

    #nomor 3
# Membuat data kamar hotel
# 3 gedung, 15 lantai, 20 kamar per lantai
kamar = [[[False for k in range(20)] for l in range(15)] for g in range(3)]

# Menampilkan sebagian data (contoh gedung 1)
print("Gedung 1:")
for lantai in kamar[0]:
    print(lantai)

# Contoh: ada tamu di gedung 2, lantai 10, kamar 14
kamar[1][9][13] = True

print("\nSetelah ada tamu:")
print("Gedung 2, Lantai 10:", kamar[1][9])

#nomor 4
def pesan(angka):
    print("Masukkan sebuah angka:", angka)

pesan(10)

#nomor 5
hasil = [i * 3 for i in range(1, 11) if i % 2 == 0]

print(hasil)

#nomor 6
# Membuat array 2 dimensi 3x3 berisi angka 1 sampai 9
array_2d = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# Menampilkan seluruh isi array
print("Isi array 2 dimensi 3x3:")
for i in range(len(array_2d)):
    for j in range(len(array_2d[i])):
        print(array_2d[i][j], end=" ")
    print()  # Untuk pindah baris setelah satu baris selesai

#nomor 7
data = [[2, 4], [6, 8], [10, 12]]

# Cara flatten
hasil = []
for sublist in data:
    for item in sublist:
        hasil.append(item)

print(hasil)


#nomor 8
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# memanggil fungsi
hasil = luas_persegi_panjang(8, 5)

print("Luas persegi panjang =", hasil)