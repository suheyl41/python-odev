def katmaDegerCiro():
    a=int(input("toplamSatisMiktari:"))
    b=int(input("hammaddeMaliyeti:"))
    c=int(input("bakimOnarimGiderleri:"))
    d=int(input("sevkiyatGiderleri:"))
    e=int(input("satinAlinanHizmetGiderleri:"))
    katmaDegerCiro=a-(b+c+d+e)
    if (katmaDegerCiro>=1000):
        print("İşletme katma değer cirosu yüksek")
    elif (katmaDegerCiro>=500) and (katmaDegerCiro<1000):
        print("İşletme katma değer cirosu normal")
    else:
        print("İşletme katma değer cirosu düşüktür")

