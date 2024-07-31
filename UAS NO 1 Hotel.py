import tkinter as tk
from tkinter import ttk

class HotelApp:
    def __init__(self, master):
        self.master = master
        master.title("Hotel 'SEJUK ASRI' Pemesanan Kamar")

        # Frame untuk input field
        input_frame = tk.Frame(master)
        input_frame.pack()

        # Label dan Entry widget untuk input field
        tk.Label(input_frame, text="Nama Petugas:").grid(row=0, column=0, padx=5, pady=5)
        self.petugas_entry = tk.Entry(input_frame)
        self.petugas_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Nama Customer:").grid(row=1, column=0, padx=5, pady=5)
        self.customer_entry = tk.Entry(input_frame)
        self.customer_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Tanggal Check-in:").grid(row=2, column=0, padx=5, pady=5)
        self.checkin_entry = tk.Entry(input_frame)
        self.checkin_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Pilih Kode Kamar:").grid(row=3, column=0, padx=5, pady=5)
        self.kamar_combobox = ttk.Combobox(input_frame, values=["M", "S", "L", "A"])
        self.kamar_combobox.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Lama Sewa (hari):").grid(row=4, column=0, padx=5, pady=5)
        self.lamasewa_entry = tk.Entry(input_frame)
        self.lamasewa_entry.grid(row=4, column=1, padx=5, pady=5)

        # Tombol untuk memproses input
        self.process_button = tk.Button(input_frame, text="Proses", command=self.process_input)
        self.process_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Frame untuk output field
        output_frame = tk.Frame(master)
        output_frame.pack()

        # Label untuk judul output
        tk.Label(output_frame, text="Bukti Pemesanan Kamar", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        tk.Label(output_frame, text="Hotel 'SEJUK ASRI'", font=("Arial", 12)).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Label dan Entry widget untuk output field
        tk.Label(output_frame, text="Nama Petugas:").grid(row=2, column=0, padx=5, pady=5)
        self.petugas_output = tk.Label(output_frame, text="")
        self.petugas_output.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Nama Customer:").grid(row=3, column=0, padx=5, pady=5)
        self.customer_output = tk.Label(output_frame, text="")
        self.customer_output.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Tanggal Check-in:").grid(row=4, column=0, padx=5, pady=5)
        self.checkin_output = tk.Label(output_frame, text="")
        self.checkin_output.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Nama Kamar:").grid(row=5, column=0, padx=5, pady=5)
        self.kamar_output = tk.Label(output_frame, text="")
        self.kamar_output.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Harga Sewa:").grid(row=6, column=0, padx=5, pady=5)
        self.harga_output = tk.Label(output_frame, text="")
        self.harga_output.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Lama Sewa:").grid(row=7, column=0, padx=5, pady=5)
        self.lamasewa_output = tk.Label(output_frame, text="")
        self.lamasewa_output.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="PPN 10%:").grid(row=8, column=0, padx=5, pady=5)
        self.ppn_output = tk.Label(output_frame, text="")
        self.ppn_output.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Jumlah Bayar:").grid(row=9, column=0, padx=5, pady=5)
        self.jumlahbayar_output = tk.Label(output_frame, text="")
        self.jumlahbayar_output.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Total Bayar:").grid(row=10, column=0, padx=5, pady=5)
        self.totalbayar_output = tk.Label(output_frame, text="")
        self.totalbayar_output.grid(row=10, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Uang Bayar:").grid(row=11, column=0, padx=5, pady=5)
        self.uangbayar_entry = tk.Entry(output_frame)
        self.uangbayar_entry.grid(row=11, column=1, padx=5, pady=5)

        tk.Label(output_frame, text="Uang Kembali:").grid(row=12, column=0, padx=5, pady=5)
        self.uangkembali_output = tk.Label(output_frame, text="")
        self.uangkembali_output.grid(row=12, column=1, padx=5, pady=5)

    def process_input(self):
        # Dapatkan nilai input dari input field
        petugas = self.petugas_entry.get()
        customer = self.customer_entry.get()
        checkin = self.checkin_entry.get()
        kamar = self.kamar_combobox.get()
        lamasewa = int(self.lamasewa_entry.get())

        # Hitung harga berdasarkan tipe kamar
        if kamar == "M":
            harga = 650000
        elif kamar == "S":
            harga = 550000
        elif kamar == "L":
            harga = 400000
        elif kamar == "A":
            harga = 350000
        else:
            harga = 0

        # Hitung total harga berdasarkan lama menginap
        jumlahbayar = harga * lamasewa

        # Hitung PPN berdasarkan lama menginap
        if lamasewa > 5:
            ppn = jumlahbayar * 0.1
        elif lamasewa > 3:
            ppn = jumlahbayar * 0.05
        else:
            ppn = 0

        # Hitung total harga setelah menambahkan PPN
        totalbayar = jumlahbayar + ppn

        # Tampilkan output pada output field
        self.petugas_output.config(text=petugas)
        self.customer_output.config(text=customer)
        self.checkin_output.config(text=checkin)
        self.kamar_output.config(text=kamar)
        self.harga_output.config(text=f"Rp. {harga:,}") # Tambahkan "Rp." dan format koma dengan 2 desimal
        self.lamasewa_output.config(text=lamasewa)
        self.ppn_output.config(text=f"Rp. {ppn:,}") # Tambahkan "Rp." dan format koma dengan 2 desimal
        self.jumlahbayar_output.config(text=f"Rp. {jumlahbayar:,}") # Tambahkan "Rp." dan format koma dengan 2 desimal
        self.totalbayar_output.config(text=f"Rp. {totalbayar:,}") # Tambahkan "Rp." dan format koma dengan 2 desimal

        # Hitung kembalian ketika customer membayar
        try:
            uangbayar_str = self.uangbayar_entry.get()
            uangbayar_str = uangbayar_str.replace(".", "")  # Hapus titik
            uangbayar_str = uangbayar_str.replace(",", ".")  # Ganti koma dengan titik
            uangbayar = float(uangbayar_str)
            uangkembali = uangbayar - totalbayar
            self.uangkembali_output.config(text=f"Rp. {uangkembali:,}") # Tambahkan "Rp." dan format koma dengan 2 desimal
        except ValueError:
            self.uangkembali_output.config(text="Input valid uang bayar")

# Buat jendela utama dan jalankan aplikasi
root = tk.Tk()
app = HotelApp(root)
root.mainloop()