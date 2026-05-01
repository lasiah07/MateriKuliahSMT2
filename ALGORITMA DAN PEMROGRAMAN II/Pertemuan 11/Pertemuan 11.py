#nomor 1
def fungsi_sederhana():
    print("Halo!")
    return

fungsi_sederhana()

#nomor 2
def cek_status(status):
    print("Status:", status)
    return

cek_status(False)

#nomor 3
def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print(hasil)

#nomor 4
def tambah(a, b):
    return a + b

# 1. Mengabaikan hasil return
tambah(3, 5)

# 2. Disimpan ke variabel
hasil = tambah(3, 5)
print("Disimpan:", hasil)

# 3. Langsung ditampilkan
print("Langsung:", tambah(10, 2))

#nomor 5
def cek_data(data):
    if data == "":
        return None
    return data

hasil = cek_data("")
print(hasil)

#nomor 6
def tampilkan_list(data):
    for item in data:
        print(item)

angka = [1, 2, 3, 4, 5]

tampilkan_list(angka)

#nomor 7
def tampilkan_list(data):
    for item in data:
        print(item)
    print("-----")  # pembatas biar rapi

# Pemanggilan dengan argumen berbeda-beda
tampilkan_list([1, 2, 3])
tampilkan_list(["apel", "jeruk", "mangga"])
tampilkan_list([10, 20, 30])

#nomor 8
def buat_list():
    data = [1, 2, 3, 4, 5]
    return data

hasil = buat_list()
print(hasil)

#nomor 9
def tahun_kabisat(tahun):
    # Tahun kabisat:
    # habis dibagi 4 dan tidak habis dibagi 100
    # atau habis dibagi 400
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False


data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "->", end=" ")
    
    hasil = tahun_kabisat(th)
    
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

#nomor 10
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False
def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30
data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]
for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(thn, bln, "->", end="")

    hasil = hari_didalam_bulan(thn, bln)

    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

#nomor 11
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return None  # bulan tidak valid
def hari_pada_tahun(tahun, bulan, hari):
    # cek bulan valid
    if bulan < 1 or bulan > 12:
        return None

    # cek hari valid
    jumlah_hari = hari_didalam_bulan(tahun, bulan)
    if hari < 1 or hari > jumlah_hari:
        return None

    total = 0

    # jumlahkan hari dari bulan sebelumnya
    for b in range(1, bulan):
        total += hari_didalam_bulan(tahun, b)

    # tambah hari di bulan sekarang
    total += hari

    return total
# contoh pemanggilan
print(hari_pada_tahun(2000, 12, 31))

#nomor 12
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    
    return True


for i in range(1, 20):
    if cek_prima(i):
        print(i, end=" ")

#nomor 13
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    
    return True


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")

print()

#nomor 14
def Liter100km_ke_mpg(liter):
    # 1 mil = 1.609344 km
    # 1 gallon = 3.785411784 liter
    mil = 100 / 1.609344          # ubah 100 km ke mil
    galon = liter / 3.785411784   # ubah liter ke gallon
    return mil / galon
def mpg_ke_Liter100km(mpg):
    km100 = 100 / 1.609344        # 100 km ke mil
    liter = 3.785411784           # 1 gallon ke liter
    return liter / (mpg / km100)
# output sesuai soal
print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))