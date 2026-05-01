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