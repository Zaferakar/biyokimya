enzim_miktarı = float(input('Enzim miktarı (µmol:'))
enzimin_parantez_içindeki_mA_değeri = float(input('Enzimin parantez içindeki Ma değerini giriniz:'))
katalizlenen_substrat_miktarı = float(input('Katalizlenen substrat miktarı(µmol/dakika):'))
alt_unite_sayısı = float(input('Alt ünite sayısı:'))

turnover_sayısı = katalizlenen_substrat_miktarı*(enzimin_parantez_içindeki_mA_değeri/enzim_miktarı)

print('m/Ma dan molekül sayısı bulunur. ')
print('')
print(enzim_miktarı,'µg enzim',katalizlenen_substrat_miktarı,'µmol/dakika çeviriyorsa')
print('')
print('1 molekül enzim',turnover_sayısı ,'µmol/dakika substratı çevirir.')
print('')
print('m:',enzimin_parantez_içindeki_mA_değeri,'turnover sayısı:',katalizlenen_substrat_miktarı,'x',enzimin_parantez_içindeki_mA_değeri,'/',enzim_miktarı)
#mikro gramdan mikro mole dönüşüm var o yüzden bölüyoruz, turnover sayısı bir enzim molekülü tarafından çevrilen substrat molekül sayısıdır.
print('')
print('mikro gramdan mikro mole dönüşüm var o yüzden bölüyoruz, turnover sayısı bir enzim molekülü tarafından çevrilen substrat molekül sayısıdır.')
print('')
print('Turnover sayısı:',turnover_sayısı,'µmol/dakika')
print('')
print('Enzim',alt_unite_sayısı,'alt ünite içeriyorsa',alt_unite_sayısı,'tane aktif bölge içeriyor demektir')
print('Katalitik merkez aktivitesini hesaplamak için turnover sayısını aktif bölge sayısına böleriz')
print('')
print('Katalitik merkez aktivitesi',turnover_sayısı/alt_unite_sayısı,'dir')




