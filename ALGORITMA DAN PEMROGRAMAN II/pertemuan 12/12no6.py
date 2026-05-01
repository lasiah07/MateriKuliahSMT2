def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))
c = float(input("Masukkan sisi c: "))

if cek_segitiga(a, b, c):
    print("Bisa membentuk segitiga")
else:
    print("Tidak bisa membentuk segitiga")