secret_number = 7

print("=== Game Tebak Angka Rahasia Pesulap ===")
print("Pesulap telah memilih sebuah angka antara 1 sampai 10")
print("Coba tebak angka tersebut!")

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan == secret_number:
        print("Selamat! Tebakan kamu benar!")
        break
    else:
        print("Salah! Coba tebak lagi.")