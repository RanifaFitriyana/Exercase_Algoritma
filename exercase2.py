gaji_karyawan = {}
nama = str(input('Masukkan nama : '))
jam_kerja = int(input('Masukkan jam kerja : '))
tarif = int(input('Masukkan tarif per jam : '))

jml_jam_kerja = 20 * jam_kerja
jml_gaji = jml_jam_kerja * tarif

print(f'Nama Karyawan : {nama}')
print(f'Jumlah jam kerja dalam sebulan : {jml_jam_kerja}')
print(f'Jumlah gaji dalam sebulan : {jml_gaji}')

# Caranya rapli
# nama = str(input('Masukkan nama : '))
# jam_kerja = int(input('Masukkan jam kerja : '))
# tarif = int(input('Masukkan tarif : '))

# gaji_perbulan = jam_kerja * tarif
# gaji_perbulan *= 20
# print([nama,f'Rp{gaji_perbulan}'])
# if (gaji_perbulan < 3000000):
#     print('Gaji anda dibawah UMR')