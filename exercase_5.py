jml_siswa = int(input('Masukkan jumlah siswa : '))
nilai_ujian = []
for i in range(1, jml_siswa + 1):

    nilai = float(input('Masukkan nilai ujian siswa {i}: '))
    nilai_ujian.append(nilai)

jml_nilai = sum(nilai_ujian)
rata_rata = jml_nilai / jml_siswa

print("Rata-rata nilai dari seluruh siswa adalah : ",rata_rata)


# Caranya rapli
# jumlah_siswa = int(input('Masukkan jumlah siswa : '))
# total_nilai = 0
# for x in range(jumlah_siswa):
#     nilai = float(input('Masukkan nilai : '))
#     total_nilai += nilai

# rata_rata = total_nilai / jumlah_siswa
# print(f'Rata-rata nilai ujian siswa adalah {rata_rata:.2f}')
