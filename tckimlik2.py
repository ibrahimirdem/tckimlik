tcno = input("TC Kimlik No İlk 9 Hanesini Giriniz: ")
a, b, toplamDokuz = 0, 0, 0
for i in range(9):
    toplamDokuz = toplamDokuz+int(tcno[i])
    if i%2 == 0:
        a = a+7*int(tcno[i])
    elif i%2 == 1:
        b = b+int(tcno[i])
    if i == 8:
        haneOn = (a-b)%10
        haneOnBir = (haneOn+toplamDokuz)%10
        print(tcno+str(haneOn)+str(haneOnBir))
