data = [
    ["Nama", "Usia", "Kota"],
    ["Andi", 20, "Jakarta"],
    ["Budi", 22, "Bandung"],
    ["Citra", 19, "Surabaya"]
]

for baris in data:
    for kolom in baris:
        print(kolom, end=" | ")
    print()