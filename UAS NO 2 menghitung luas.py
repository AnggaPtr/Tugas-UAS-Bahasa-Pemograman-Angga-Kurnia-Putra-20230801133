# Modul untuk menghitung luas dan keliling bangun datar
def luas_persegi(sisi):
    return sisi ** 2

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(alas, tinggi):
    return alas + tinggi + (alas ** 2 + tinggi ** 2) ** 0.5

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari ** 2

def keliling_lingkaran(jari_jari):
    return 2 * 3.14 * jari_jari

# Menu utama
def main():
    while True:
        print("Menu Utama:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            sisi = float(input("Masukkan sisi persegi: "))
            print("Luas Persegi:", luas_persegi(sisi))
            print("Keliling Persegi:", keliling_persegi(sisi))

        elif pilihan == "2":
            panjang = float(input("Masukkan panjang persegi panjang: "))
            lebar = float(input("Masukkan lebar persegi panjang: "))
            print("Luas Persegi Panjang:", luas_persegi_panjang(panjang, lebar))
            print("Keliling Persegi Panjang:", keliling_persegi_panjang(panjang, lebar))

        elif pilihan == "3":
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            print("Luas Segitiga:", luas_segitiga(alas, tinggi))
            print("Keliling Segitiga:", keliling_segitiga(alas, tinggi))

        elif pilihan == "4":
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            print("Luas Lingkaran:", luas_lingkaran(jari_jari))
            print("Keliling Lingkaran:", keliling_lingkaran(jari_jari))

        elif pilihan == "5":
            print("Hatur Nuhun Parantos Ngajalan Keun Program Ieu ^0^")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()