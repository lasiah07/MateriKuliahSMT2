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