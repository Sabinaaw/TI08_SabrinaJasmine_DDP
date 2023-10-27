# no. 1 menentukan kategori usia seseorang
#deklarasi variabel
nama = 'kim dokja'
usia = 28

#kondisi if
if(usia < 18 ):
    kategori = 'Anak-Anak'
elif(usia >= 18 and usia < 65):
    kategori = 'Dewasa'
else:
    kategori = 'Lanjut Usia'

#cetak data
print(nama, 'merupakan kategori', kategori)

print()

# no. 2 menentukan angka yang lebih besar
# deklarasi variabel
x = 9
y = 20
z = 15

# kondisi if
if x < z and y > z:
    print('Y yang terbesar')
elif x < y and y > z:
    print('Z yang terbesar')
else :
    ('X yang terbesar')

