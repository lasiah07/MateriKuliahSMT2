# Penanganan Key (Metode.get())
config = {"host":"localhost","port":8080}

#Cara Berbahaya (Akan Error jika 'timeout' tidak ada)
#print (config["timeout"])

#Cara Aman(Menggunakan nilai default jika key tidak ada)
timeout = config.get("timeout",30) #jika tidak ada, beri nilai 30
print(f"Timeout yang digunakan : {timeout} detik")

#Mengecek Keberadaan Key secara efisien (O(1))
if "host" in config:
    print(f"Server berjalan di:{config['host']}")