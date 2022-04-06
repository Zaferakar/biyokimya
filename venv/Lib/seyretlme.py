istenilen_çözelti_hacim = float(input('istenilen Çözeltinin hacim:'))
istenilen_yüzde_derişimi = float(input('istenilen yüzdelik çözelti:'))
ilk_çözeltinin_derişimi = float(input('İlk çözeltinin derişimi:'))


alınamsı_gereken_hacim = (100/ilk_çözeltinin_derişimi)*istenilen_çözelti_hacim*(istenilen_yüzde_derişimi/100)

print('oranında seyreltilmeli:',alınamsı_gereken_hacim/istenilen_çözelti_hacim)