try:
    saldo = 100000  # saldo awal
    ambil = int(input("Masukkan jumlah uang yang ingin diambil: "))

    hasil = saldo - ambil

    if ambil <= 0:
        raise ValueError("Jumlah harus lebih dari 0")
    elif ambil > saldo:
        raise Exception("Saldo tidak cukup")

    print("Uang berhasil diambil")
    print("Sisa saldo:", hasil)

except ValueError:
    print("Error: input harus berupa angka dan tidak boleh nol/negatif")

except Exception as e:
    print("Error:", e)