secret_number = 777

print(
"""
+================================+
| Selamat datang di game saya, muggle! |
| masukkan suatu angka dan tebak |
| angka berapa yang saya pilih   |
| untuk kamu.                    |
| Jadi, berapa angka rahasianya? |
+================================+
"""
)

guess = int(input("Masukkan angka: "))

while guess != secret_number:
    print("hahaha! kamu nyangkut di Loop saya")
    guess = int(input("Coba lagi: "))

print("Selamat, Muggle! kamu bebas sekarang!")