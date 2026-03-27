import streamlit as st
import re

st.title("📊 Word Frequency Analyzer (BERT-ready)")

# 1. Program menerima input paragraf teks panjang
text_input = st.text_area("Masukkan paragraf teks untuk dianalisis:", placeholder="Contoh: belajar struktur data itu seru belajar python juga seru")

if st.button("Hitung Frekuensi"):
    if text_input:
        # 2. Bersihkan teks dari simbol (titik, koma, dll) menggunakan Regex
        clean_text = re.sub(r'[^\w\s]', '', text_input).lower()
        words_list = clean_text.split()

        # 3. Gunakan Dictionary untuk menghitung frekuensi
        # Key: Kata, Value: Frekuensi
        word_count_dict = {}
        for word in words_list:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

        # 4. Tampilkan daftar kata unik dan jumlahnya dalam tabel Streamlit
        st.subheader("Hasil Analisis Kata Unik")
        
        # Mengonversi dictionary ke format yang rapi untuk tabel
        data_tabel = [{"Kata": k, "Frekuensi": v} for k, v in word_count_dict.items()]
        st.table(data_tabel)
        
        st.success(f"Total kata unik ditemukan: {len(word_count_dict)}")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")