gereken_enzim_miktarı = float(input('Gereken enzim miktarı:'))
hatalar_için_yüzdelik_fazla_alınan = float(input('Yüzde olarak kaç katını aldınız:'))

toplam_ihtiyaç_duyulan_enzim = gereken_enzim_miktarı*((hatalar_için_yüzdelik_fazla_alınan+100)/100)


print('Toplam ihtiyaç duyulan enzim miktarı:',gereken_enzim_miktarı,'(10 üssünü yaz)x',hatalar_için_yüzdelik_fazla_alınan+100,'/',100)
print('')

print('Toplam ihtiyaç duyulan enzim miktarı:',toplam_ihtiyaç_duyulan_enzim,'(10 üssünü yaz)ünite')
print('')
print('1 katal = 6x10 üssü 7 ünite')
print('')
print(toplam_ihtiyaç_duyulan_enzim,'/6x10 üssü 7 (kaç katal olduğunu elinle hesapla)')
