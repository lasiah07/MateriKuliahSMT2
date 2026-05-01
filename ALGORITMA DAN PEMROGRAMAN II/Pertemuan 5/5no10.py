pendapatan = float(input("masukkan pendapatan bulanan :"))
pajak = 0
pendapatan_tahun = pendapatan * 12
if pendapatan_tahun <= 60000000 :
    pajak = pendapatan_tahun * 0.05
elif pendapatan_tahun <= 250000000:
    pajak = pendapatan_tahun * 0.15
elif pendapatan_tahun <= 500000000 :
    pajak = pendapatan_tahun * 0.25
else :
    pajak = pendapatan_tahun * 0.30
print ("pajak penghasilan yang harus anda bayar adalah",pajak,"rupiah" )