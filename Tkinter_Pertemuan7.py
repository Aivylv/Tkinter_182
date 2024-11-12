import tkinter as tk  #mengimpor modul tkinter sebagai tk untuk membuat GUI
from tkinter import messagebox  #mengimpor messagebox dari tkinter untuk menampilkan pesan error

def hasil_prediksi():  #fungsi untuk menghitung dan menampilkan hasil prediksi
    try:
        for entry in entries:  #loop untuk mengambil setiap nilai input
            nilai = int(entry.get())  #mengambil nilai dari input dan mengubahnya menjadi integer
            if not (0 <= nilai <= 100):  #mengecek apakah nilai berada dalam rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")  #jika tidak, lempar error
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  #jika input valid, tampilkan hasil prediksi
    except ValueError as ve:  #jika terjadi error (input bukan angka atau di luar rentang)
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")  #tampilkan pesan error

#Buat GUI dengan Tkinter
root = tk.Tk()  #membuat jendela utama GUI
root.title("Aplikasi Prediksi Prodi Pilihan")  #mengatur judul jendela
root.geometry("500x600")  #mengatur ukuran jendela (500x600 piksel)
root.configure(bg="#FBA0B5")  #mengatur warna latar belakang jendela


#Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 20))  #membuat label judul dengan font besar
judul_label.pack(pady=20)  #menampilkan label judul dan memberi jarak vertikal (padding) 20 piksel

#Input Nilai Mata Pelajaran
frame_input = tk.Frame(root, bg="#F4C2C2")  #membuat frame untuk menampung input nilai mata pelajaran
frame_input.pack(pady=10)  #menampilkan frame dengan jarak vertikal 10 piksel


#Input nilai mata pelajaran
entries = []  #membuat list kosong untuk menyimpan objek Entry
for i in range(10):  #loop untuk membuat 10 kolom input
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran ({i + 1}):", font=("Arial", 12))  #membuat label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  #menempatkan label di kolom kiri dengan padding dan rata kanan
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  #membuat kolom input (Entry) untuk nilai mata pelajaran
    entry.grid(row=i, column=1, padx=10, pady=5)  #menempatkan kolom input di kolom kanan dengan padding
    entries.append(entry)  #menambahkan setiap kolom input ke dalam list entries

#Button "Hasil Prediksi"
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  #membuat tombol untuk memicu prediksi
prediksi_button.pack(pady=30)  #menampilkan tombol dan memberi jarak vertikal 30 piksel

#Label luaran hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"))  #membuat label untuk menampilkan hasil prediksi
hasil_label.pack(pady=20)  #menampilkan label hasil prediksi dengan jarak vertikal 20 piksel

#Jalankan GUI
root.mainloop()  #menjalankan loop utama GUI, agar jendela tetap terbuka dan merespons interaksi pengguna