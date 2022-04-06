import math
zayıf_asit_hacmi_litre = float(input('Zayıf asidin litre bazında hacmini giriniz:'))
zayıf_asit_molaritesi = float(input('Zayıf asidin Molaritesini giriniz:'))
zayıf_bazın_molaritesi = float(input('Zayıf bazın molaritesinin giriniz:'))
pKa = float(input('İyonlaşma sabitini giriniz:'))

pKa2 = -math.log10(pKa)

pH = (pKa2-math.log10(zayıf_asit_molaritesi))/2
print('zayıf asitlerde pH denklemi')
print('pH:(pKa+p[HA])/2:',pH)


zayıf_bazın_hacmi_litre = float(input('eklenen zayıf bazın hacmi:'))
baz_mol = zayıf_bazın_hacmi_litre*zayıf_bazın_molaritesi
print('n = M x V ,Eklenen bazın mol sayısı', baz_mol)
print('Geriye kalan HA miktarı = [orijinal HA miktarı] - [A-] ye titre olan [HA] miktarı')
asit_mol = zayıf_asit_hacmi_litre*zayıf_asit_molaritesi
Geriye_kalan_HA_miktarı_mol = asit_mol - baz_mol
print('Geriye kalan HA miktarı(mol cinsinden):',Geriye_kalan_HA_miktarı_mol )

print('Titrasyon boyunca herhangi bir noktada pH pH=pKa + log[Aüssü eksi]/[HA] formülü ile hesaplanır(eklenen bazın hacmine ve molaritesine bağlıdır).')
titrasyon_boyunca_herhangi_bir_noktada_pH = pKa + math.log10(baz_mol/Geriye_kalan_HA_miktarı_mol)
print('Titrasyon boyunca herhangi bir noktada pH(eklenen hacme göre değişir):', titrasyon_boyunca_herhangi_bir_noktada_pH)

print('grafik çizimi:')
print('Y kordinat sistemi = pH dır , X kordinat sistemi eklenen OH dır.' )
print('Y kordinat düzlemindekiler, a = pH:',pH )
print(' b = baz eklenince oluşan pH dır(hacime bağlı):',titrasyon_boyunca_herhangi_bir_noktada_pH)
print('c = iyonlaşma sabiti(pKa):',pKa)
print('e = son , X te b = eklenen baz hacmi :',zayıf_bazın_hacmi_litre)

print('Son noktadaki pH ,pKb(zayıf bazın iyonlaşma sabiti) den hesaplanır')
print('Kb = [HA].[OH]/[A üzeri eksi]')
print('(pOH = pKb + p[A üzeri eksi])/2')

pKb_zayıf_bazın_iyonlaşma_sabiti = 14-pKa2
print('zayıf bazın iyonlaşma sabiti:', pKb_zayıf_bazın_iyonlaşma_sabiti)

A_mol = zayıf_asit_hacmi_litre*zayıf_asit_molaritesi
pA = -math.log10(A_mol)
print('A üzeri eksi:',pA)

pOH = (pKb_zayıf_bazın_iyonlaşma_sabiti + pA)/2
print('pOH:', pOH)
print('pH:',14-pOH)



