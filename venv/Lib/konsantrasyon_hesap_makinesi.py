import sys
while True:
    print('Konsantrasyon hesap makinesine hoşgeldiniz')
    print('')
    print('Molarite Hesaplamak İçin 1\'e tıklayın.')
    print('Molalite Hesaplamak için 2\'ye tıklayın.')
    print('Normalite Hesaplamak için 3\'ye tıklayın.')
    print('Mol kesri Hesaplamak için 4\'ye tıklayın.')
    print('Programdan çıkmak için q\'ya tıklayın.')
    print('')

    giris = input('İşlem numarasını giriniz:')

    if giris == '1':
        çözünenin_mol_sayısı = float(input('Çözünenin mol sayısını giriniz:'))
        çözeltinin_hacmi = float(input('Çözeltinin hacmini giriniz(Litre):'))
        print('Çözeltinin molaritesi:',çözünenin_mol_sayısı/çözeltinin_hacmi,'(M)Molar')

    elif giris == '2':
        çözünen_madde_miktarı_mol = float(input('Çözünen maddenin mol miktarını giriniz::'))
        çözeltinin_kütlesi = float(input('Çözeltinin kütlesini giriniz(Kg):'))
        print('Çözeltinin molalitesi:',çözünen_madde_miktarı_mol/çözeltinin_kütlesi,'(m)Molal')
    elif giris == '3':
        çözünen_eşdeğer_gram_sayısı = float(input('Çözünen eşdeğer gram sayısını giriniz:'))
        çözeltininn_hacmi = float(input('Çözeltinin hacmini giriniz(Litre):'))
        print('Çözeltinin normalitesi:', çözünen_eşdeğer_gram_sayısı/çözeltininn_hacmi,'(N)Normalite')

    elif giris == '4':
        istediğiniz_bileşenin_ismi = input('İstediğiniz bileşenin ismini giriniz:')
        istediğiniz_bileşenin_mol_değeri = float(input('İstediğiniz bileşenin mol değerini giriniz:'))
        toplam_mol_değeri = float(input('Toplam mol değerini giriniz:'))
        print(istediğiniz_bileşenin_ismi,'bileşeninin mol kesri:',istediğiniz_bileşenin_mol_değeri/toplam_mol_değeri)

    elif giris == 'q' or 'Q':
        print('Programdan çıkılıyor...')
        sys.exit()

    else:
        print('Hatalı işlem')

    continue