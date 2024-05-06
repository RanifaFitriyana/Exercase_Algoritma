# Caranya ranifa
my_book = {}
judul = str(input('Masukkan Judul Buku : '))
tahun = int(input('Masukkan Tahun Terbit : '))
harga = float(input('Masukkan Harga Buku : '))
penulis = str(input('Masukkan Penulis : '))
ketersediaan = bool(input('Masukkan Ketersediaan Buku (kosongkan jika tidak ada): '))

my_book['judul'] = judul
my_book['tahun'] = tahun
my_book['harga'] = harga
my_book['penulis'] = penulis
my_book['ketersediaan'] = ketersediaan

print(my_book)

# Caranya rapli
# buku = []
# judul_buku = str(input('Masukkan judul buku : '))
# tahun_terbit = int(input('Masukkan tahun terbit : '))
# harga = float(input('Masukkan harga : '))
# penulis = str(input('Masukkan penulis : '))
# stock = bool(input('Masukkan ketersediaan buku (kosongkan jika tidak ada) : '))

# buku.append(judul_buku)
# buku.append(tahun_terbit)
# buku.append(harga)
# buku.append(penulis)

# print(buku)

# if (stock == True):
#     print('Sedia')
# else:
#     print('Stock buku kosong')