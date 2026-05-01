data = [[2, 4], [6, 8], [10, 12]]

# Cara flatten
hasil = []
for sublist in data:
    for item in sublist:
        hasil.append(item)

print(hasil)
