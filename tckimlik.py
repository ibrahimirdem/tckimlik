# -*- coding: cp1254 -*-
#TC Kimlik No Son 2 Haneyi Bulma!

#TC No adinda bir fonksiyon icersinde bu islerimizi yapiyoruz.
def tcno(tcno):
    # TC kimlik nosunun ilk 9 hanesini istedigimiz icin fazlasi veya
    #azini bize verirse asagida else ile hata yazdiriyoruz.
    if len(tcno) == 9:
        # Burada girilen TC NO nun 1, 3, 5, 7, ve 9. hanelerini alip topluyor ve
        #7 ile carpiyoruz ve a adinda bir degiskene atadik.
        #Ama dikkat pythonda ilk hane sifirdan basladigi icin 0, 2, 4, 6 ve 8 diyerek
        #bu hanelere ulasiyoruz.
        a = 7*(int(tcno[0])+int(tcno[2])+int(tcno[4])+int(tcno[6])+int(tcno[8]))
        # Buradada ayni sekilde 2, 4, 6 ve 8. haneleri alip topluyoruz.
        b = int(tcno[1])+int(tcno[3])+int(tcno[5])+int(tcno[7])
        # Buldugumuz bu a ve b degiskenlerinin farkini alip mod(10) = %10 ile
        #10 a bolumunden kalani bize 10. haneyi veriyor. Bunu haneOn degiskenine
        #atadik
        haneOn = (a-b)%10
        #Ilk 9 haneye 10. haneyide ekleyip 10 haneli sayimizi olusturduk.
        onHaneli=str(tcno)+str(haneOn)
        # Burada for ile bu onHaneli deki 10 haneyi toplayıp toplamOn degiskenine
        #atiyoruz.
        toplamOn = 0
        for i in range(10):
            toplamOn=toplamOn+int(onHaneli[i])
        #Sirada toplanilan ilk 10 hanenin mod(10) alarak yani 10 a bolumunden kala-
        #nini bularak 11. haneyi bulup bunun haneOnBir degiskenine atiyoruz.
        haneOnBir = toplamOn%10
        #En son olarak ilk 9 hane 10. hane ve 11. haneyi birlestirip cikti veriyoruz
        return tcno+str(haneOn)+str(haneOnBir)
    else:
        print "Girilen TC No 9 Haneli Olmalidir."


#raw_input ile ilk 9 haneyi kullanicidan aliyoruz.
tcnumara = raw_input("TC Kimlik No Ilk 9 Hanesini Giriniz:")
#Daha sonra burada tcno() fonk. icine bu numarayi atayip ciktiyi aliyoruz.
print "TC Kimlik No'nun Tamami :",tcno(tcnumara)
