botol = [20, 15, 25, 10]

for i in range(len(botol)):
    for j in range(len(botol)-1):
        if botol[j] > botol[j+1]:
            # tukar posisi
            botol[j], botol[j+1] = botol[j+1], botol[j]

print("Urutan botol:", botol)