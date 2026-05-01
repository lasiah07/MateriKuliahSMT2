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