while True:
    dilüsyon_oranı = float(input('Dilüsyon oranı(x/10):'))
    absorbans_degeri = float(input('Absorbans değeri(A260):'))
    konstrasyon_değeri = float(input('Konsantrasyon değeri(µg/ml):'))
    print('')


    if konstrasyon_değeri == 50:
        print(konstrasyon_değeri,'µg/ml  dsDNA A260 = 1 değerini verir')
        print('')
        print('X . 1 =',konstrasyon_değeri,'µg/ml .',absorbans_degeri)
        print('X =',konstrasyon_değeri*absorbans_degeri,'µg/ml dilüsyon sonrası')
        print('konsatrasyonu eski haline getirmek için seyreltme oranının tersi ile çarpıyoruz')
        print('dilüsyon oranı:',(dilüsyon_oranı/10),'Seyreltme oranının tersi',((dilüsyon_oranı/10)**-1),'çarparsak:',konstrasyon_değeri*absorbans_degeri*((dilüsyon_oranı/10)**-1),'µg/ml= orijinal dsDNA konsantrasyonu')

    elif konstrasyon_değeri == 40:
        print(konstrasyon_değeri,'µg/ml ssRNA A260 = 1 değerini verir')
        print('')
        print('X . 1 =', konstrasyon_değeri, 'µg/ml .', absorbans_degeri)
        print('X =', konstrasyon_değeri * absorbans_degeri, 'µg/ml dilüsyon sonrası')
        print('konsatrasyonu eski haline getirmek için seyreltme oranının tersi ile çarpıyoruz')
        print('dilüsyon oranı:', (dilüsyon_oranı / 10), 'Seyreltme oranının tersi', ((dilüsyon_oranı / 10) ** -1),'çarparsak:', konstrasyon_değeri * absorbans_degeri * ((dilüsyon_oranı / 10) ** -1),'µg/ml= orijinal ssRNA konsantrasyonu')

    elif konstrasyon_değeri == 35:
        print(konstrasyon_değeri,'µg/ml ssDNA A260 = 1 değerini verir')
        print('')
        print('X . 1 =', konstrasyon_değeri, 'µg/ml .', absorbans_degeri)
        print('X =', konstrasyon_değeri * absorbans_degeri, 'µg/ml dilüsyon sonrası')
        print('konsatrasyonu eski haline getirmek için seyreltme oranının tersi ile çarpıyoruz')
        print('dilüsyon oranı:', (dilüsyon_oranı / 10), 'Seyreltme oranının tersi', ((dilüsyon_oranı / 10) ** -1),'çarparsak:', konstrasyon_değeri * absorbans_degeri * ((dilüsyon_oranı / 10) ** -1),'µg/ml= orijinal ssDNA konsantrasyonu')

    elif konstrasyon_değeri == 20:
        print(konstrasyon_değeri,'µg/ml ss oligo DNA A260 = 1 değerini verir')
        print('')
        print('X . 1 =', konstrasyon_değeri, 'µg/ml .', absorbans_degeri)
        print('X =', konstrasyon_değeri * absorbans_degeri, 'µg/ml dilüsyon sonrası')
        print('konsatrasyonu eski haline getirmek için seyreltme oranının tersi ile çarpıyoruz')
        print('dilüsyon oranı:', (dilüsyon_oranı / 10), 'Seyreltme oranının tersi', ((dilüsyon_oranı / 10) ** -1),'çarparsak:', konstrasyon_değeri * absorbans_degeri * ((dilüsyon_oranı / 10) ** -1),'µg/ml= orijinal ss oligo DNA konsantrasyonu')


    else:
        print()

    continue