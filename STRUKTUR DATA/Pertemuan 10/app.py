import streamlit as st
from stack_backend import StackLinkedList, cek_kurung, balik_string

st.set_page_config(
    page_title="Blue Stack Lab",
    page_icon="🌊",
    layout="wide"
)

# ===== STYLE =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1a2a, #112f4a);
}

.title {
    font-size: 2.5rem;
    color: #66d9ff;
    text-align: center;
    font-weight: bold;
}

.card {
    background: #0f2a44;
    border: 1px solid #1f4e79;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
}

.stack-box {
    background: #0d2236;
    padding: 15px;
    border-radius: 10px;
}

.stack-item {
    background: #1c4f7a;
    color: white;
    padding: 10px;
    margin: 5px 0;
    border-radius: 5px;
}

.top {
    background: #66d9ff;
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===== SESSION =====
if "stack" not in st.session_state:
    st.session_state.stack = StackLinkedList()

# ===== TITLE =====
st.markdown('<div class="title">🌊 BLUE STACK LAB</div>', unsafe_allow_html=True)

menu = st.sidebar.selectbox("Menu", [
    "Stack",
    "Cek Kurung",
    "Balik String"
])

# ===== STACK =====
if menu == "Stack":
    st.subheader("Stack Playground")

    col1, col2 = st.columns(2)

    with col1:
        val = st.text_input("Input")

        if st.button("Push"):
            if val:
                st.session_state.stack.push(val)

        if st.button("Pop"):
            try:
                st.session_state.stack.pop()
            except:
                st.warning("Stack kosong!")

        if st.button("Clear"):
            st.session_state.stack.clear()

    with col2:
        items = st.session_state.stack.to_list()

        if not items:
            st.write("Stack kosong")
        else:
            for i, item in enumerate(items):
                if i == 0:
                    st.markdown(f'<div class="stack-item top">{item} (TOP)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="stack-item">{item}</div>', unsafe_allow_html=True)

# ===== CEK KURUNG =====
elif menu == "Cek Kurung":
    st.subheader("Cek Kurung")

    ekspresi = st.text_input("Masukkan ekspresi")

    if st.button("Cek"):
        valid, _ = cek_kurung(ekspresi)

        if valid:
            st.success("Seimbang ✅")
        else:
            st.error("Tidak Seimbang ❌")

# ===== BALIK STRING =====
elif menu == "Balik String":
    st.subheader("Balik String")

    teks = st.text_input("Masukkan teks")

    if st.button("Balik"):
        hasil = balik_string(teks)
        st.info(f"Hasil: {hasil}")