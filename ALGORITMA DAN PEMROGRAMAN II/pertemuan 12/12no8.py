def cek_segitiga(a, b, c):
    # cek dulu apakah bisa membentuk segitiga
    if not (a + b > c and b + c > a and c + a > b):
        return "Tidak bisa membentuk segitiga"
    # cek jenis segitiga
    if a == b == c:
        return "Segitiga Sama Sisi"
    elif a == b or b == c or a == c:
        return "Segitiga Sama Kaki"
    else:
        return "Segitiga Sembarang"
# input user
a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))
c = float(input("Masukkan sisi c: "))
# output
hasil = cek_segitiga(a, b, c)
print(hasil)