# III. Implementasi Cybersecurity (IP Threat Intel)

#Database IP berbahaya (industri Biasanya menggunakan Dictionary atau set)
# Key : IP Address, Value: Jenis Serangan
threat_intel = {
    "192.168.1.50":"DDoS Attack",
    "10.0.0.12":"SQL Injection",
    "172.16.0.5":"Malware Callback"

} 

def scan_network(ip_list):
    print("---Memulai Pemindaian Jaringan---")
    for ip in ip_list:
        #Pencarian di Dictionary bernilai O(1)
        found_threat = threat_intel.get(ip)
        if found_threat:
            print(f"[BAHAYA]{ip} Teridentifikasi sebagai {found_threat}!")
        else :
            print(f"[AMAN]{ip} tidak ditemukan dalam database ancaman.")

#simulasi log masuk
logs = ["192.168.1.1","10.0.0.12","192.168.1.50","8.8.8.8"]
scan_network(logs)
