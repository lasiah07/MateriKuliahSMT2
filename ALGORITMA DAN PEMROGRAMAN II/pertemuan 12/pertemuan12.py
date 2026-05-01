#nomor 1
def contoh():
    x = 10
    return x

hasil = contoh()
print(hasil)

#nomor 2
x = 10  # variable global

def contoh():
    print("Nilai x di dalam fungsi:", x)

contoh()
print("Nilai x di luar fungsi:", x)

#nomor 3
x = 10  # variable global

def contoh(a):
    print("Nilai a di dalam fungsi:", a)

contoh(x)

#nomor 4
x = 10  # variable global

def ubah_nilai():
    global x   # ⬅️ keyword global
    x = x + 5  # ubah nilai x

ubah_nilai()
print(x)

#nomor 5
def hitung_imt(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100  # konversi cm ke meter
    imt = berat / (tinggi_m ** 2)
    return imt

# input dari user
berat = float(input("Masukkan berat badan (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

# hitung IMT
index_massa_tubuh = hitung_imt(berat, tinggi_cm)

# kategori
kategori = ["Normal", "Gemuk", "Obesitas"]

# menentukan kategori berdasarkan IMT
if 18.5 <= index_massa_tubuh <= 25.0:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[0])
elif 25.0 < index_massa_tubuh <= 27.0:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[1])
else:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori",
           kategori[2], ". Anda harus diet!")
    
#nomor 6
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

#nomor 7
def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(1, 1, 1))  # True
print(cek_segitiga(1, 1, 3))  # False

#nomor 8
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

#nomor 9
def faktorial(n):
    # bilangan harus >= 0
    if n < 0:
        return None
    
    # 0! dan 1! = 1
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(1, n + 1):
        hasil = hasil * i
    
    return hasil

# input user
n = int(input("Masukkan nilai yang ingin di faktorial: "))

# output
print(n, "! =", faktorial(n))

#nomor 10
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    hasil_jumlah = 0
    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1, elem_2 = elem_2, hasil_jumlah
    return hasil_jumlah

for n in range(1, 10):
    print(n, "->", fibonacci(n))

#nomor 11
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Contoh penggunaan
print(faktorial(5))  # Output: 120 (karena 5! = 5*4*3*2*1 = 120)

#nomor 12
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Contoh penggunaan
for i in range(1, 10):
    print(f"Fib({i}) = {fibonacci(i)}")