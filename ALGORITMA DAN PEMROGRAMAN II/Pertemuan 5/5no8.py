a = int(input("masukkan nilai Matematika:"))
b = int(input("masukkan nilai Bahasa Indonesia:"))
c = int(input("masukkan nilai Bahasa Inggris:"))

if a>b and a>c :
    terbesar = a
elif b>a and b>c :
    terbesar = b
else :
    terbesar = c
print ("nilai tertinggi :" , terbesar)