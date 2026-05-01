def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Contoh penggunaan
for i in range(1, 10):
    print(f"Fib({i}) = {fibonacci(i)}")