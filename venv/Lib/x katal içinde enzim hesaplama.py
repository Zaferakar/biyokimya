liste = []
liste1 = []
muamele_sayisi = int(input('Muamele sayısını giriniz:'))
tekerrür_sayisi = int(input('Tekerrür sayısını giriniz:'))

for y in range(muamele_sayisi):
    muamele_ismi = input('Muamele ismini giriniz:')
    for k in range(tekerrür_sayisi):
        a = int(input("{} Muamelesinin {}. tekerrür degerini  giriniz :".format(muamele_ismi, k+1)))
        liste1.append(a)
    liste.append(liste1)

    liste1 = []
print(liste)