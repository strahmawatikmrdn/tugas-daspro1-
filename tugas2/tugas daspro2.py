hari_kerja = 4
hari_kerja_perbulan = 16
gaji = 1000000000
gaji_lembur_perjam = 20000000

total = (hari_kerja/hari_kerja_perbulan)*gaji+gaji_lembur_perjam
total= int(total)
total_gaji =F"{total:,}"
print ("Rp",total_gaji)