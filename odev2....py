def kullanilabilirlik():
    a=int(input("Planlanmış Üretim Süresi:"))
    b=int(input("Plansız Duruş:"))
    kullanilabilirlik=(a-b)/a
    print(kullanilabilirlik)
def performans():
    c=int(input("Standart Çevrim Zamanı:"))
    d=int(input("Üretim Miktarı:"))
    a=int(input("Planlanmış Üretim Süresi:"))
    b=int(input("Plansız Duruş:"))
    performans=(c*d)/(a-b)
    print(performans)
def kalite():
    e=int(input("Sağlam Ürün Miktarı:"))
    f=int(input("Toplam Üretim Miktarı:"))
    kalite=e/f
    print(kalite)
def oee():
    a=int(input("Planlanmış Üretim Süresi:"))
    b=int(input("Plansız Duruş:"))
    c=int(input("Standart Çevrim Zamanı:"))
    d=int(input("Üretim Miktarı:"))
    e=int(input("Sağlam Ürün Miktarı:"))
    f=int(input("Toplam Üretim Miktarı:"))
    kullanilabilirlik=(a-b)/a
    performans=(c*d)/(a-b)
    kalite=e/f
    oee=kullanilabilirlik*performans*kalite*100
    print("OEE=%",oee)
