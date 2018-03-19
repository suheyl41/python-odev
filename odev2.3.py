def ilk6AylikGelir(yazGel,finGel,urunSaGel):
    global ilk6AyTopGel
    ilk6AyTopGel=yazGel+finGel+urunSaGel
    print('İlk 6 aylık toplam geliriniz:',ilk6AyTopGel)
    return ilk6AyTopGel
def ilk6AylikGider(calMa,kiraGid,donMal):
    global ilk6AyTopGid
    ilk6AyTopGid=calMa+kiraGid+donMal
    print('İlk 6 aylık toplam gideriniz:',ilk6AyTopGid)
    return ilk6AyTopGid
def ilk6AyİsletmeKari(ilk6AyTopGel,ilk6AyTopGid):
    global ilk6AyİsKar
    ilk6AyİsKar=ilk6AyTopGel-ilk6AyTopGid
    return ilk6AyİsKar
def son6AylikGelir(yazGel,spoGel,eTicGel,urunSaGel):
    global son6AyTopGel
    son6AyTopGel=yazGel+spoGel+eTicGel+urunSaGel
    print('Son 6 aylık toplam geliriniz:',son6AyTopGel)
    return son6AyTopGel
def son6AylikGider(calMa,kiraGid,bakMal):
    global son6AyTopGid
    son6AyTopGid=calMa+kiraGid+bakMal
    print('Son 6 aylık toplam gideriniz:',son6AyTopGid)
    return son6AyTopGid
def son6AyİsletmeKari(son6AyTopGel,son6AyTopGid):
    global son6AyİsKar
    son6AyİsKar=son6AyTopGel-son6AyTopGid
    return son6AyİsKar
def karlarArasiFark(ilk6AyİsKar,son6AyİsKar):
    fark=ilk6AyİsKar-son6AyİsKar
    print('İşletme karları arasındaki fark:',fark)
    if (fark>5000):
        print('İşletme çok karlı.')
    elif (fark>=1000):
        print('İşletme karı normal.')
    else:
        print('İşletme yeterince karda değil.')
print('İlk 6 aylık gelirlerinizi yazınız')
yazGel=int(input('Yazılım gelirlerinizi yazınız:'))
finGel=int(input('Finansman gelirlerinizi yazınız:'))
urunSaGel=int(input('Ürün satış gelirinizi yazınız:'))
print('İlk 6 aylık giderlerinizi yazınız')
calMa=int(input('Çalışan maaşlarını giriniz:'))
kiraGid=int(input('Kira giderlerinizi giriniz:'))
donMal=int(input('Donanım maliyetinizi giriniz:'))
ilk6AyGelir=ilk6AylikGelir(yazGel,finGel,urunSaGel)
ilk6AyGider=ilk6AylikGider(calMa,kiraGid,donMal)
ilk6AyİsletmeKari(ilk6AyGelir,ilk6AyGider)
print('İlk 6 aylık İşletme karınız:',ilk6AyİsKar)
print('Son 6 aylık gelirlerinizi yazınız')
yazGel=int(input('Yazılım gelirlerinizi yazınız:'))
spoGel=int(input('Sponsorluk gelirinizi giriniz:'))
eTicGel=int(input('E ticaret gelirinizi giriniz:'))
urunSaGel=int(input('Ürün satış gelirinizi yazınız:'))
print('Son 6 aylık giderlerinizi yazınız')
calMa=int(input('Çalışan maaşlarını giriniz:'))
kiraGid=int(input('Kira giderlerinizi giriniz:'))
bakMal=int(input('Bakım maliyetinizi giriniz:'))
son6AyGelir=son6AylikGelir(yazGel,spoGel,eTicGel,urunSaGel)
son6AyGider=son6AylikGider(calMa,kiraGid,bakMal)
son6AyİsletmeKari(son6AyGelir,son6AyGider)
print('Son 6 aylık işletme karınız:',son6AyİsKar)
a=ilk6AyİsletmeKari(ilk6AyTopGel,ilk6AyTopGid)
b=son6AyİsletmeKari(son6AyTopGel,son6AyTopGid)
karlarArasiFark(a,b)
