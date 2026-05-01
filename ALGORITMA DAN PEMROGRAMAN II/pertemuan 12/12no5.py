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