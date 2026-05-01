def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Contoh penggunaan
print(faktorial(5))  # Output: 120 (karena 5! = 5*4*3*2*1 = 120)