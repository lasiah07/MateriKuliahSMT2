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