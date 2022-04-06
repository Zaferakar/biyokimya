reaksiyon_sonrası_obsorbans_fark = float(input('Reaksiyon sonrası obsorbasyon farkı:'))
reaksiyonun_verimi = float(input('Reaksiyonun yüzdelik verimini giriniz:'))
molar_konsantrasyon_sabiti = float(input('Molar konsantrasyon sabitini giriniz(Em):'))
molar_konsantrasyon_sabitinin_virgülden_sonraki_kısmı = float(input('Molar konsantrasyon sabitinin virgülden sonraki kısmı:'))

sonuc = (reaksiyon_sonrası_obsorbans_fark/molar_konsantrasyon_sabiti)*reaksiyonun_verimi/100

print('')
print('%100 dönüşüm olduğunda',reaksiyon_sonrası_obsorbans_fark,'fark:',reaksiyon_sonrası_obsorbans_fark,'/',molar_konsantrasyon_sabiti,molar_konsantrasyon_sabitinin_virgülden_sonraki_kısmı,'mol/L ye denk gelir')

print('')
print('%',reaksiyonun_verimi,'dönüşüyor','(',reaksiyonun_verimi,'/100',')x','(',reaksiyon_sonrası_obsorbans_fark,'/',molar_konsantrasyon_sabiti,'x',molar_konsantrasyon_sabitinin_virgülden_sonraki_kısmı,')mol/L' )
print('')
print('ölçümdeki konsantrasyon:',sonuc,'x',molar_konsantrasyon_sabitinin_virgülden_sonraki_kısmı,'(10 üssü olarak yaz)mol/L')
print('ölçümdeki konsantrasyon:',sonuc*1000*molar_konsantrasyon_sabitinin_virgülden_sonraki_kısmı,'mmol/L')