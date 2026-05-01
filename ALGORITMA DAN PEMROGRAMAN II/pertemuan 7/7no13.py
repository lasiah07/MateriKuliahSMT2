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