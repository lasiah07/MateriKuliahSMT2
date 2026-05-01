kata = input("Masukkan sebuah kata: ")

kata = kata.upper()

for huruf in kata:
    if huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
        continue
    else:
        print(huruf)