#1mL glikoz(bilinmeyen konsantrasyon) standart kolorimetrik method ile ölçüldü(1 mL of 200 µg/mL), OD_bilinmeyen = 0.1
#OD_standart = 0.2 Bu değerlere göre bilinmeyen konsantrasyon değeri nedir?

glikoz_miktarının_hacmi = float(input('Glikoz miktarının hacmi(mL):'))
OD_unknown_bilinmeyen = float(input('Bilinmeyen OD değeri:'))
OD_standart = float(input('Standat OD değeri:'))
glikoz_miktarının_hacminin_yoğunluğu = float(input('Glikoz miktarının hacminin yoğunluğu(µg/mL):'))

def bilinmeyen_konsantrasyon_hesaplama (glikoz_miktarının_hacmi,OD_unknown_bilinmeyen,OD_standart,glikoz_miktarının_hacminin_yoğunluğu):
    bilinmeyen_konsantrasyon = (OD_unknown_bilinmeyen*glikoz_miktarının_hacminin_yoğunluğu)/OD_standart
    print('Bilinmeyen konsantrasyon:',bilinmeyen_konsantrasyon)

bilinmeyen_konsantrasyon_hesaplama(glikoz_miktarının_hacmi,OD_unknown_bilinmeyen,OD_standart,glikoz_miktarının_hacminin_yoğunluğu)

