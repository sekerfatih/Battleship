
#MUHAMMET FATİH ŞEKER   18010011038

from random import randint

f=1

while(f==1):
    boyut = int(input("Oyun alanı için 9'dan büyük sayı giriniz: "))

    alan = []

    gemi = []
    açıkalan = []
    gem = 0
    gemibir = 0
    gemiiki = 0
    gemiüç = 0

    for r in range(0,4):
        gemii = []
        for m in range(0,4):
            sütun = []
            for n in range(0,2):
                sütun.append(0)
            gemii.append(sütun)
        gemi.append(gemii)


    for x in range(0,boyut):
        alan.append(["?"]*boyut)

    def print_alan(alan):
        for row in alan:
            print((" ").join(row))

    for x in range(0,boyut):
        açıkalan.append(["?"]*boyut)

    def print_açıkalan(açıkalan):
        for row in açıkalan:
            print((" ").join(row))


    def random_sütun(alan):
        return randint(0,boyut-1)
    def random_satır(alan):
        return randint(0,boyut-1)

    def random_sütun_bir(alan):
        return randint(0,boyut-2)
    def random_satır_bir(alan):
        return randint(0,boyut-2)

    def random_sütun_iki(alan):
        return randint(0,boyut-3)
    def random_satır_iki(alan):
        return randint(0,boyut-3)

    def random_sütun_üç(alan):
        return randint(0,boyut-4)
    def random_satır_üç(alan):
        return randint(0,boyut-4)

    x=x1=x2=x3=y=y1=y2=y3=r=r1=r2=r3=r4=r5=t=t1=t2=t3=t4=t5=0


    x = random_satır(alan)
    y = random_sütun(alan)

    açıkalan[x][y] = "o"

    a = 0

    while (a == 0):

        x1 = random_satır_bir(alan)
        y1 = random_sütun_bir(alan)

        if (açıkalan[x1][y1] != "o"):

            k = 2
            k = randint(0,1)

            if(k == 0 and açıkalan[x1+1][y1] != "o"):
                açıkalan[x1][y1] = "o"
                açıkalan[x1+1][y1] = "o"
                r=1
                break

            elif(k == 1 and açıkalan[x1][y1+1] != "o"):
                açıkalan[x1][y1] = "o"
                açıkalan[x1][y1+1] = "o"
                t=1
                break

            else:
                continue

        else:
            continue


    a=0

    while (a == 0):

        x2 = random_satır_iki(alan)
        y2 = random_sütun_iki(alan)

        if (açıkalan[x2][y2] != "o"):

            u = 2
            u = randint(0,1)

            if (u == 0 and açıkalan[x2+1][y2] != "o" and açıkalan[x2+2][y2] != "o"):

                açıkalan[x2][y2] = "o"
                açıkalan[x2+1][y2] = "o"
                açıkalan[x2+2][y2] = "o"
                r1=1
                r2=2

                break

            elif (u == 1 and açıkalan[x2][y2+1] != "o" and açıkalan[x2][y2+2] != "o"):

                açıkalan[x2][y2] = "o"
                açıkalan[x2][y2+1] = "o"
                açıkalan[x2][y2+2] = "o"
                t1=1
                t2=2

                break


            else:
                continue


        else:
            continue

    a=0

    while (a == 0):

        x3 = random_satır_üç(alan)
        y3 = random_sütun_üç(alan)

        if (açıkalan[x3][y3] != "o"):

            m = 2
            m = randint(0, 1)

            if (m == 0 and açıkalan[x3 + 1][y3] != "o" and açıkalan[x3 + 2][y3] != "o" and açıkalan[x3 + 3][y3] != "o"):
                açıkalan[x3][y3] = "o"
                açıkalan[x3 + 1][y3] = "o"
                açıkalan[x3 + 2][y3] = "o"
                açıkalan[x3 + 3][y3] = "o"
                r3 = 1
                r4 = 2
                r5 = 3
                a = 1
                break

            elif (m == 1 and açıkalan[x3][y3 + 1] != "o" and açıkalan[x3][y3 + 2] != "o" and açıkalan[x3][
                y3 + 3] != "o"):

                açıkalan[x3][y3] = "o"
                açıkalan[x3][y3 + 1] = "o"
                açıkalan[x3][y3 + 2] = "o"
                açıkalan[x3][y3 + 3] = "o"
                t3 = 1
                t4 = 2
                t5 = 3
                a = 1
                break

            else:
                continue

        else:
            continue

    kullanılan = 0

    mod = int(input("Kapalı Mod için 1'e\nAçık Mod için 2'ye basınız: "))

    if (mod == 1):

        while ((boyut * boyut) // 3 != kullanılan):

            print_alan(alan)

            x4 = int(input("Satır: "))
            y4 = int(input("Sütun: "))
            print("\n")

            if (x4 > boyut - 1 or y4 > boyut - 1):
                print("Alanın dışına taştınız! Tekrar deneyiniz.\n")
                kullanılan += 1


            elif (açıkalan[x4][y4] == "x" or açıkalan[x4][y4] == "*"):
                print("Bu noktayı zaten vurdunuz! Tekrar deneyiniz.\n")
                kullanılan += 1

            elif (x4 == x and y4 == y):
                print("Tebrikler bir gemiyi batırdınız!\n")
                alan[x4][y4] = "x"
                kullanılan += 1
                gem = 1

            elif (x1 == x4 and y1 == y4 or x1 + r == x4 and y1 + t == y4):
                print("Tebrikler bir gemiyi vurdunuz!\n")
                gemibir += 1
                alan[x4][y4] = "x"
                kullanılan += 1

                if (gemibir == 2):
                    print("Ve batırdınız!\n")


            elif (x2 == x4 and y2 == y4 or x2 + r1 == x4 and y2 + t1 == y4 or x2 + r2 == x4 and y2 + t2 == y4):

                print("Tebrikler bir gemiyi vurdunuz!\n")

                gemiiki += 1

                alan[x4][y4] = "x"
                kullanılan += 1

                if (gemiiki == 3):
                    print("Ve batırdınız!\n")


            elif (
                    x3 == x4 and y3 == y4 or x3 + r3 == x4 and y3 + t3 == y4 or x3 + r4 == x4 and y3 + t4 == y4 or x3 + r5 == x4 and y3 + t5 == y4):

                print("Tebrikler bir gemiyi vurdunuz!\n")

                gemiüç += 1

                alan[x4][y4] = "x"
                kullanılan += 1

                if (gemiüç == 4):
                    print("Ve batırdınız!\n")


            else:
                print("İsabet ettiremediniz!\n")
                alan[x4][y4] = "*"
                kullanılan += 1

            if ((boyut * boyut) // 3 == kullanılan):
                print("\n")
                print("Maalesef Kaybettiniz.\n")
                f = int(input("Devam etmek için 1'e\n"
                              "Oyundan çıkmak için 2'ye basınız: "))
                print("\n")
                break

            elif (gem + gemibir + gemiiki + gemiüç == 10):
                puan = ((boyut * boyut) // 3) - kullanılan
                print("\n")
                print("Tebrikler {} puan ile kazandınız!\n".format(puan))
                f = int(input("Devam etmek için 1'e\n"
                              "Oyundan çıkmak için 2'ye basınız: "))
                print("\n")
                break

            else:
                continue


    elif (mod == 2):

        while ((boyut * boyut) // 3 != kullanılan):

            print_açıkalan(açıkalan)

            x4 = int(input("Satır: "))
            y4 = int(input("Sütun: "))
            print("\n")

            if (x4 > boyut - 1 or y4 > boyut - 1):
                print("Alanın dışına taştınız! Tekrar deneyiniz.\n")
                kullanılan += 1


            elif (açıkalan[x4][y4] == "x" or açıkalan[x4][y4] == "*"):
                print("Bu noktayı zaten vurdunuz! Tekrar deneyiniz.\n")
                kullanılan += 1

            elif (x4 == x and y4 == y):
                print("Tebrikler bir gemiyi batırdınız!\n")
                açıkalan[x4][y4] = "x"
                kullanılan += 1
                gem = 1

            elif (x1 == x4 and y1 == y4 or x1 + r == x4 and y1 + t == y4):
                print("Tebrikler bir gemiyi vurdunuz!\n")
                gemibir += 1
                açıkalan[x4][y4] = "x"
                kullanılan += 1

                if (gemibir == 2):
                    print("Ve batırdınız!\n")


            elif (x2 == x4 and y2 == y4 or x2 + r1 == x4 and y2 + t1 == y4 or x2 + r2 == x4 and y2 + t2 == y4):

                print("Tebrikler bir gemiyi vurdunuz!\n")

                gemiiki += 1

                açıkalan[x4][y4] = "x"
                kullanılan += 1

                if (gemiiki == 3):
                    print("Ve batırdınız!\n")


            elif (
                    x3 == x4 and y3 == y4 or x3 + r3 == x4 and y3 + t3 == y4 or x3 + r4 == x4 and y3 + t4 == y4 or x3 + r5 == x4 and y3 + t5 == y4):

                print("Tebrikler bir gemiyi vurdunuz!\n")

                gemiüç += 1

                açıkalan[x4][y4] = "x"
                kullanılan += 1

                if (gemiüç == 4):
                    print("Ve batırdınız!\n")


            else:
                print("İsabet ettiremediniz!\n")
                açıkalan[x4][y4] = "*"
                kullanılan += 1

            if ((boyut * boyut) // 3 == kullanılan):
                print("\n")
                print("Maalesef Kaybettiniz.\n")
                f = int(input("Devam etmek için 1'e\n"
                              "Oyundan çıkmak için 2'ye basınız: "))
                print("\n")
                break

            elif (gem + gemibir + gemiiki + gemiüç == 10):
                puan = ((boyut * boyut) // 3) - kullanılan
                print("\n")
                print("Tebrikler {} puan ile kazandınız!\n".format(puan))
                f=int(input("Devam etmek için 1'e\n"
                            "Oyundan çıkmak için 2'ye basınız: "))
                print("\n")
                break


    else:
        print("Hatalı tuşlama yaptınız.")
        break