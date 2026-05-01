topi_list = [1, 2, 3, 4, 5]

# Langkah 1
topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))

# Langkah 2
del topi_list[-1]

# Langkah 3
print(len(topi_list))

print(topi_list)