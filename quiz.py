import streamlit as st
import requests

# Judul aplikasi
st.title("Contoh Penggunaan Radio Button di Streamlit")

# Radio button
opsi = st.radio(
    "Pilih salah satu topik:",
    ("Beranda", "Tentang", "Kontak")
)

# Tampilkan konten berdasarkan pilihan
if opsi == "Beranda":
    st.header("Selamat datang di Beranda!")
    st.write("Ini adalah halaman utama dari aplikasi Streamlit Anda.")
elif opsi == "Tentang":
    st.header("Tentang Aplikasi")
    st.write("Aplikasi ini dibuat menggunakan Streamlit dan menunjukkan cara menggunakan radio button.")
elif opsi == "Kontak":
    st.header("Hubungi Kami")
    st.write("Silakan kirim email ke: info@example.com")


# Judul aplikasi
st.title("Contoh Penggunaan Selectbox di Streamlit")

# Selectbox untuk memilih bahasa pemrograman favorit
bahasa = st.selectbox(
    "Pilih bahasa pemrograman favorit Anda:",
    ["Python", "JavaScript", "C++", "Java", "Go", "Rust"]
)

# Menampilkan pilihan pengguna
st.write(f"Anda memilih: **{bahasa}**")

# Tampilkan deskripsi berdasarkan pilihan
if bahasa == "Python":
    st.write("🐍 Python sangat populer untuk data science, web, dan otomasi.")
elif bahasa == "JavaScript":
    st.write("🌐 JavaScript digunakan di hampir semua website modern.")
elif bahasa == "C++":
    st.write("⚙️ C++ digunakan untuk aplikasi yang butuh performa tinggi.")
elif bahasa == "Java":
    st.write("☕ Java banyak digunakan di perusahaan besar dan aplikasi Android.")
elif bahasa == "Go":
    st.write("🚀 Go sangat cepat dan cocok untuk aplikasi cloud dan server.")
elif bahasa == "Rust":
    st.write("🦀 Rust terkenal aman dan efisien untuk sistem-level programming.")


# Judul aplikasi
st.title("Contoh Penggunaan Multiselect di Streamlit")

# Multiselect untuk memilih hobi
hobi = st.multiselect(
    "Pilih hobi Anda:",
    ["Membaca", "Menulis", "Bermain Musik", "Bermain Game", "Olahraga", "Memasak"]
)

# Menampilkan pilihan
if hobi:
    st.write("Hobi yang Anda pilih:")
    for item in hobi:
        st.write(f"- {item}")
else:
    st.write("Anda belum memilih hobi apa pun.")

st.title("Isi Google Form via Python")

nama = st.text_input("Nama")
kelas = st.text_input("Kelas")
jawaban = st.text_input("Jawaban")

if st.button("Kirim"):
    if nama and kelas and jawaban:
        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfKrfBjr6tN3lXKrfDwupOwBp1ZmfekeGKmMFCzJ4iZZO5TJg/formResponse"

        data = {
            "entry.6791275": nama,   # Ganti dengan entry ID dari form
            "entry.383486237": kelas,   # Ganti dengan entry ID dari form
            "entry.1086114307": jawaban,   # Ganti dengan entry ID dari form
        }

        response = requests.post(url, data=data)
        if response.status_code == 200:
            st.success("Berhasil dikirim!")
        else:
            st.error(f"Gagal mengirim. Status code: {response.status_code}")
    else:
        st.warning("Mohon isi semua data.")
