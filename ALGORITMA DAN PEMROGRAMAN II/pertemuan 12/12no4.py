x = 10  # variable global

def ubah_nilai():
    global x   # ⬅️ keyword global
    x = x + 5  # ubah nilai x

ubah_nilai()
print(x)