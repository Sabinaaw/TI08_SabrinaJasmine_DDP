# no. 1
kendaraan=['kdr001', 'Honda CBR250RR', 249.7, 'merah']

# no. 2
kendaraan.append('Rp. 63,634,000')
kendaraan.append(2)
kendaraan.insert(2, 'Honda')
kendaraan.insert(3, 'Ravery Mat Red')

print(kendaraan)

# no. 3
import math

def hitung_luas(bentuk, *args):
    match bentuk:
        case "persegi":
            sisi = args[0]
            luas_persegi = sisi ** 2
            return luas_persegi
        case "lingkaran":
            jari_jari = args[0]
            luas_lingkaran = math.pi * jari_jari ** 2
            return luas_lingkaran
        case "segitiga":
            alas, tinggi = args[0], args[1]
            luas_segitiga = 0.5 * alas * tinggi
            return luas_segitiga
        case _:
            return "Salah memasukkan pilihan"

# Contoh pemanggilan fungsi
print("Luas Persegi:", hitung_luas("persegi", 4))
print("Luas Lingkaran:", hitung_luas("lingkaran", 3))
print("Luas Segitiga:", hitung_luas("segitiga", 4, 5))
print("Luas Segiempat:", hitung_luas("segiempat", 4, 5))  # Contoh bentuk tidak valid
