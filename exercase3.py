list_pekerjaan = ['Dokter','PNS','Pilot','Pengusaha']

nama = str(input('Masukkan Nama : '))
umur = int(input('Masukkan Umur : '))
pekerjaan_ortu = str(input('Masukkan Pekerjaan Ortu : '))
gaji_ortu = int(input('Masukkan Gaji Ortu : '))
ipk = float(input('Masukkan IPK : '))

if pekerjaan_ortu not in list_pekerjaan and gaji_ortu <= 1000000 and ipk >= 2.7 and umur < 25:
    print('Anda berhak mendapatkan beasiswa')
else:
    print('Anda tidak berhak mendapatkan beasiswa')

# pekerjaanlist = ("PNS,Tentara")
# nama = str(input("Masukkan Nama : "))
# pekerjaan = str(input("Masukkan Pekerjaan Ortu : "))
# umur = int(input("Masukkan Umur : "))
# gaji_ortu = int(input("Masukkan Gaji Ortu : "))
# ipk = float(input("Masukkan IPK anda : "))

# if pekerjaan not in pekerjaanlist and gaji_ortu <= 1000000 and ipk >= 2.5 and umur < 25:
#     print('selamat anda dpt beasiswa')
# else:
#     print('nice try')

# pekerjaan_ortu = ['Dokter','PNS','Pilot','Pengusaha']
# kerjaan = '' if pekerjaan_ortu 
# gaji_ortu <= 1000000
# ipk >= 2.7
# umur < 25

# if pekerjaan_ortu == True and absensi >= 70:
#     print('Boleh Ujian')
# else :
#     print('Tidak boleh ujian')

# x = 4
# hasil = 'Besar' if x > 5 else 'Kecil'
# print(hasil)

# if x > 10:
#     print('Besar')
# else:
#     print('Kecil')