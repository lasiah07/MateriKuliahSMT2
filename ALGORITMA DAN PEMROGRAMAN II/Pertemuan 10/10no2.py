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