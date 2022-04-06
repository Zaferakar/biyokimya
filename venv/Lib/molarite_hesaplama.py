yüz_gram_stok_cozelti_konsantrasyonunda_bulunan_madde_miktari= float(input('Stok çözelti konsantrasyonunu giriniz:'))
molekul_kutlesi = float(input('molekülün kütlesini giriniz:'))

su_miktari =  100 - yüz_gram_stok_cozelti_konsantrasyonunda_bulunan_madde_miktari

bin_gramda_bulunan_madde_miktari = yüz_gram_stok_cozelti_konsantrasyonunda_bulunan_madde_miktari * 1000 / su_miktari

mol_miktari = bin_gramda_bulunan_madde_miktari/molekul_kutlesi

molalite= mol_miktari / 1
print('molalite:', molalite)
