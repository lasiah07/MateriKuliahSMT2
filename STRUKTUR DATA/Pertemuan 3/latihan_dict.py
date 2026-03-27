# 1. Membuat Dictionary (Analogi Profil User LinkedIn)
user_profile = {
    "username": "firdaus_cyber",
    "role": "Researcher",
    "skills": ["Python", "BERT", "LSTM"],
    "is_active": True
}

# 2. Akses Data (O(1))
print(f"Mencari Role: {user_profile['role']}")

# 3. Menambah/Update Data
user_profile["location"] = "Cirebon"
user_profile["role"] = "Senior Researcher"

# 4. Dictionary Comprehension (Efisien)
# Misal: Mengubah daftar skor menjadi status aman/tidak
scores = {"IP_1": 90, "IP_2": 45, "IP_3": 85}
security_status = {k: ("Aman" if v > 70 else "Bahaya") for k, v in scores.items()}

print("Status Keamanan:", security_status)


