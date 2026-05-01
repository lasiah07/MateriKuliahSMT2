def Liter100km_ke_mpg(liter):
    # 1 mil = 1.609344 km
    # 1 gallon = 3.785411784 liter
    mil = 100 / 1.609344          # ubah 100 km ke mil
    galon = liter / 3.785411784   # ubah liter ke gallon
    return mil / galon
def mpg_ke_Liter100km(mpg):
    km100 = 100 / 1.609344        # 100 km ke mil
    liter = 3.785411784           # 1 gallon ke liter
    return liter / (mpg / km100)
# output sesuai soal
print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))