#nomor 1
makanan = input("Masukkan makanan favorit: ") 
print("Makanan favorit kamu adalah:", makanan)

#nomor 2
def bilangan_bulat(): 
    angka = 10 
    print(angka) 
bilangan_bulat()

#nomor 3
print("string") #disini saya menggunakan input string
a = (input("masukkan angka pertama:"))
b = (input("masukkan angka kedua:"))
print ("hasil penjumlahan :" , a+b )

print("Integer") #disini saya menggunakan input dan integer
a = (int(input("masukkan angka pertama:")))
b = (int(input("masukkan angka kedua:")))
print ("hasil penjumlahan :" , a+b )

#nomor 4
a = float(input("Masukkan angka pertama: ")) 
b = float(input("Masukkan angka kedua: ")) 
print("Hasil pembagian:", a / b) 

#nomor 5
alas = float(input("masukkan panjang alas :")) 
tinggi = float(input("masukkan panjang tinggi:")) 
hypo = (alas**2 + tinggi**2)** 0.5 
print("maka panjang sisi miring adalah :", hypo)

#nomor 6
alas = float(input("masukkan panjang alas :")) 
tinggi = float(input("masukkan panjang tinggi:")) 
print("maka panjang sisi miring adalah :", ((alas**2 + tinggi**2)**0.5))

#nomor 7
jumlah = 8 
print ("jumlah apel cia ada :" + str(jumlah)) 

#nomor 8
print("Replikasi pada string") 
print("ha"*3) 
print("Replikasi pada list") 
jumlah = [1,2] 
print(jumlah * 3)

#nomor 9
nilai = 4.00 
IPK = str(nilai) 
print("Cia mendapatkan IPK :" + IPK)

#nomor 10
angka = 12 
print(type (angka)) 
nilai = 4.00 
print(type(nilai)) 

#nomor 11
# input nilai dari user 
a = float(input("Masukkan nilai a: ")) 
b = float(input("Masukkan nilai b: ")) 
# operasi matematika 
print("Hasil penjumlahan:", a + b) 
print("Hasil pengurangan:", a - b) 
print("Hasil pembagian:", a / b) 
print("Hasil perkalian:", a * b) 
# kalimat tambahan 
print("Selamat kamu sudah pintar matematika") 

#nomor 12
x = float(input("Masukkan nilai x: ")) 
y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x))) 
print("Hasil y =", y)

#nomor 13
jam = int(input("Waktu mulai (jam): ")) 
menit = int(input("Waktu mulai (menit): ")) 
durasi = int(input("Durasi Acara (menit): ")) 
# tambahkan durasi ke menit 
menit += durasi 
# hitung tambahan jam dari menit 
jam += menit // 60 
# sisa menit 
menit = menit % 60 
print("Acara selesai pukul:", jam, ":", menit)