import sys

def cek_memori():
    data = []
    print(f"{'Jumlah Item':<12} | {'Ukuran Memori (Bytes)':<20}")
    print("-" * 35)
    
    for i in range(20):
        n = len(data)
        b = sys.getsizeof(data)
        print(f"{n:<12} | {b:<20}")
        data.append(i)

if __name__ == "__main__":
    cek_memori()



