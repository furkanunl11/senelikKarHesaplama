

k = 0

while k == 0:

    yatirmakistenenTutar = float(input("\nKripto paraya yatirmak istedigin tutari gir.\n"))

    istenilenZaman = int(input("\nGun sayisi giriniz.\n"))

    istenilenYuzde = float(input("\nYuzde oranini giriniz.\n"))

    karSonucu = 0


    for i in range(istenilenZaman):

        yatirmakistenenTutar =  yatirmakistenenTutar+(yatirmakistenenTutar*(istenilenYuzde/100))
        karSonucu = yatirmakistenenTutar

    print(karSonucu)


    secim = input("cikis icin q'ya bas.")

    if secim =="q":
        k = 1

    else:
        k = 0



