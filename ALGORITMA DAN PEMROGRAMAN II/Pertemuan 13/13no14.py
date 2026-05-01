try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")

else:
    print("Program berjalan tanpa error")

finally:
    print("Program selesai")