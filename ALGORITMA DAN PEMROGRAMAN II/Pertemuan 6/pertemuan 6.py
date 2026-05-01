#nomor 1
#contoh 1
while True :
    print("nyangkut di perulangan tak hingga")

#nomor 2
#contoh 2
counter = 5
while counter > 2:
    print (counter)
    counter -= 1

#nomor 3
jumlah = 0
ganjil = 0
genap = 0

while jumlah < 10:
    angka = int(input("Masukkan angka ke-" + str(jumlah+1) + ": "))

    if angka % 2 == 0:
        genap = genap + 1
    else:
        ganjil = ganjil + 1

    jumlah = jumlah + 1

print("Jumlah angka genap:", genap)
print("Jumlah angka ganjil:", ganjil)

#nomor 4
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

#nomor 5
# nilai 5 siswa
a = 80
b = 75
c = 90
d = 85
e = 70

nilai = [a, b, c, d, e]

tertinggi = nilai[0]

print("Nilai siswa:", nilai)

for n in nilai:
    if n > tertinggi:
        tertinggi = n

print("Nilai tertinggi di kelas adalah:", tertinggi)

#nomor 6
n = 5
hasil = 1

for i in range(n):
    hasil = hasil * 2

print("Hasil dari 2 pangkat", n, "adalah", hasil)

#nomor 7
print("Contoh break")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("Perulangan berhenti karena break\n")

print("Contoh continue")

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

print("Angka 5 dilewati karena continue")

#nomor 8
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

#nomor 9
kata = input("Masukkan sebuah kata: ")

kata = kata.upper()

for huruf in kata:
    if huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
        continue
    else:
        print(huruf)

#nomor 10
i = 1

while i <= 5:
    print("Angka:", i)
    i = i + 1
else:
    print("Perulangan selesai")

#nomor 11
for i in range(1, 6):
    print("Angka:", i)
else:
    print("Perulangan selesai")

#nomor 12
a = 10
b = 5

print(a > b and b < 10)
print(a < b or b < 10)
print(not(a > b))

#nomor 13
# Operasi Logical
a = True
b = False

print("Operasi Logical")
print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)

# Operasi Bitwise
x = 5
y = 3

print("\nOperasi Bitwise")
print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)

#nomor 14
a = 8

print("Nilai awal a =", a)

print("a << 1 =", a << 1)
print("a << 2 =", a << 2)

print("a >> 1 =", a >> 1)
print("a >> 2 =", a >> 2)

#nomor 15
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)