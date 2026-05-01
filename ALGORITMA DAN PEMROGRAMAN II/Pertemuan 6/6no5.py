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