barang = {}

while True:
    print("Menu Utama:")
    print("1. Input data barang")
    print("2. Tampil data barang")
    print("3. Delete data barang")
    print("4. Mencari data barang")
    print("5. Hitung jumlah pembelian")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        nama_barang = input("Masukkan nama barang: ").lower()
        harga = int(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
        barang[nama_barang] = {"harga": harga, "stok": stok}
        print("Data barang berhasil ditambahkan!")

    elif pilihan == "2":
        print("Daftar Barang:")
        for nama_barang, data in barang.items():
            print(f"Nama Barang: {nama_barang}")
            print(f"Harga: {data['harga']}")
            print(f"Stok: {data['stok']}")
            print("------------------------")

    elif pilihan == "3":
        nama_barang = input("Masukkan nama barang yang ingin dihapus: ").lower()
        if nama_barang in barang:
            del barang[nama_barang]
            print("Data barang berhasil dihapus!")
        else:
            print("Data barang tidak ditemukan!")

    elif pilihan == "4":
        nama_barang = input("Masukkan nama barang yang ingin dicari: ").lower()
        if nama_barang in barang:
            print(f"Nama Barang: {nama_barang}")
            print(f"Harga: {barang[nama_barang]['harga']}")
            print(f"Stok: {barang[nama_barang]['stok']}")
        else:
            print("Data barang tidak ditemukan!")

    elif pilihan == "5":
        nama_barang = input("Masukkan nama barang yang ingin dibeli: ").lower()
        if nama_barang in barang:
            jumlah_beli = int(input("Masukkan jumlah barang yang ingin dibeli: "))
            if jumlah_beli <= barang[nama_barang]["stok"]:
                total_harga = jumlah_beli * barang[nama_barang]["harga"]
                print(f"Total harga: {total_harga}")
                barang[nama_barang]["stok"] -= jumlah_beli
                print(f"Stok barang {nama_barang} sekarang: {barang[nama_barang]['stok']}")
            else:
                print("Stok barang tidak cukup!")
        else:
            print("Data barang tidak ditemukan!")

    elif pilihan == "6":
        print("Hatur Nuhun Parantos Ngajalan Keun Program Ieu ^_^ !")
        break

    else:
        print("Pilihan tidak valid!")