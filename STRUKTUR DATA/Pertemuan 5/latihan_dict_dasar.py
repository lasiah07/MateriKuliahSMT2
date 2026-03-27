# Operasi Dasar CRUD (Gudang Data)
# 1. Create : membuat Dictionary (Analogi Database User)
user_db = {
    "1001" : {"nama":"Alice", "role":"Admin", "status":"Active"},
    "1002" : {"nama":"Bob", "role":"User", "status":"Suspended"}

}

# 2. Read Mengakses data menggunakan key
print(f"Nama User 1001:{user_db['1001']['nama']}")

# 3. Update : Mengubah data atau menambah key baru
user_db["1002"]["status"] = "Active" #Mengubah status Bob
user_db["1003"]={"nama":"Charlie", "role":"Guest", "status":"Active"} #Menambah user baru

# 4. Delete : Menghapus data
del user_db["1003"]

#5. Iterari : Mengambil semua data 
print("\n---Daftar User Aktif---")
for uid, info in user_db.items():
    print(f"ID:{uid}|Nama:{info['nama']}|Role:{info['role']}")