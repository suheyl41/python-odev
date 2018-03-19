#calisSur:Çalışma Süresi
#topMusSa:Toplam müşteri sayısı
#musCalSur:Müşteri çalışma süresi
def musteriCalismaSuresi2016():
    calisSur=int(170)
    topMusSa=int(50)
    print('Çalışma süresi:',calisSur)
    print('Toplam müşteri sayısı:',topMusSa)
    global musCalSur2016
    musCalSur2016=calisSur/topMusSa
    print('2016 Yılı müşteri çalışma süresi:')
    return musCalSur2016
def musteriCalismaSuresi2017():
    calisSur=int(220)
    topMusSa=int(70)
    print('Çalışma süresi:',calisSur)
    print('Toplam müşteri sayısı:',topMusSa)
    global musCalSur2017
    musCalSur2017=calisSur/topMusSa
    print('2017 yılı müşteri çalışma süresi:')
    return musCalSur2017
def yillarArasiFark(musCalSur2016,musCalSur2017):
    yillarArasiFark=musCalSur2017-musCalSur2016
    print('Yıllar arasındaki müşteri çalışma süresi farkı:',yillarArasiFark)
calismaSure2016=musteriCalismaSuresi2016()
calismaSure2017=musteriCalismaSuresi2017()
yillarArasiFark(calismaSure2016,calismaSure2017)
