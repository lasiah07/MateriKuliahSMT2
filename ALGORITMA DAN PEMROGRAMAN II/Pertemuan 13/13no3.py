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