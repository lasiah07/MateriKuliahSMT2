import streamlit as st
import sys

st.set_page_config(page_title="Sequence Data Manager", layout="centered")

st.title("📊 Sequence Data Management (BERT-LSTM Prototype)")
st.write("Aplikasi sederhana untuk memproses kalimat menjadi sequence data.")

# Input kalimat
kalimat = st.text_area("Masukkan kalimat panjang:")

if kalimat:
    # 1. Tokenization
    tokens = kalimat.split()

    # 2. Filter kata > 3 karakter (List Comprehension)
    filtered_tokens = [kata for kata in tokens if len(kata) > 3]

    # 3. Hitung penggunaan memori
    total_memory = sys.getsizeof(filtered_tokens)
    for kata in filtered_tokens:
        total_memory += sys.getsizeof(kata)

    # Output dashboard
    st.subheader("📌 Hasil Tokenization")
    st.write(tokens)

    st.subheader("✅ Hasil Filter (> 3 karakter)")
    st.write(filtered_tokens)

    st.subheader("💾 Total Penggunaan Memori")
    st.write(f"{total_memory} bytes")

    st.success("Proses selesai!")
else:
    st.info("Silakan masukkan kalimat terlebih dahulu.")