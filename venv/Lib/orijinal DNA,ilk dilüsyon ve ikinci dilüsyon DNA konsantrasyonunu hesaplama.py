ssDNA_konsantrasyonu = float(input('ssDNA konsantrasyonu(µmol/L):'))
dilüe_edilme_oranı = float(input('dilüe edilme oranı(x/100):'))
dilüe_edilme_sayısı = float(input('dilüe edilme sayısını giriniz:'))
print('')
print('Orijinal DNA nın  konsntrasyonu:')
print('nmol/mL')
print('Orijinal ss DNA:',ssDNA_konsantrasyonu,'µmol/L')
print('nmol e çevirmek için µmol ü 1000 çarpmamızile gerekir',ssDNA_konsantrasyonu,'(µmol/L)  x 1000 =',ssDNA_konsantrasyonu,'nmol/ml')
print('pmol e çevirmek için µmol ü 1000000 ile çarpmamız gerekir',ssDNA_konsantrasyonu,'(µmol/L)  x 1000000 =',ssDNA_konsantrasyonu*1000,'pmol/ml')
print('')
print('ilk dilüsyon:')
print((dilüe_edilme_oranı/100),'nmol/ml =',(dilüe_edilme_oranı/100)*(ssDNA_konsantrasyonu*1000),'pmol/ml')
print('')
print('ikinci dilüsyon:')
print((dilüe_edilme_oranı/100)**dilüe_edilme_sayısı,'nmol/ml = ')
print(((dilüe_edilme_oranı/100)**dilüe_edilme_sayısı)*1000,'pmol/ml')