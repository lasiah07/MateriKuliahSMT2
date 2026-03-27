import streamlit as st

st.title("📊 Word Frequency Analyzer (BERT-ready)")

text_input = st.text_area("Masukkan paragraf teks untuk dianalisis:", 
                          "belajar struktur data itu seru belajar python juga seru")

if st.button("Hitung Frekuensi"):
    words = text_input.lower().split()
    # Dictionary untuk menampung hitungan
    counts = {}
    
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    st.subheader("Hasil Analisis:")
    st.write(counts)
    
    # Menampilkan dalam bar chart sederhana
    st.bar_chart(counts)

