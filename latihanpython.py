#deklarasi variable 
pelanggan = 'budi santoso'
totalBelanja = 150000

#struktur kendali if
if(totalBelanja > 100000):
    keterangan = 'Selamat Anda mendapat Hadiah'
else:
    keterangan = 'Terima kasih sudah berbelanja'

#cetak data
print('Pelanggan', pelanggan, '\nTotal belanja Anda Rp.',totalBelanja,'\n', keterangan)

print()

#deklarasi variable 
pelanggan = 'budi santoso'
totalBelanja = 80000

#struktur kendali if
if(totalBelanja > 100000):
    keterangan = 'Selamat Anda mendapat Hadiah'
else:
    keterangan = 'Terima kasih sudah berbelanja'

#cetak data
print('Pelanggan', pelanggan, '\nTotal belanja Anda Rp.',totalBelanja,'\n', keterangan)

print()
#if multi kondisi
nama = 'Budi Santoso'
nilai = 70.50

# Uji grade dengan if mutli kondisi
if(nilai >= 85 and nilai <= 100):
    grade = 'A'
elif(nilai >= 75 and nilai < 85):
    grade = 'B'
elif(nilai >= 60 and nilai < 75):
    grade = 'C'
elif(nilai >= 30 and nilai < 60):
    grade = 'D'
else :
    grade = 'E'

print(nama, 'mendapatkan grade', grade)

