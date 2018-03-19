def donBasiStok(dolapSayisi,yatakSayisi,KoltukSayisi):
    global donemBasiStok
    donemBasiStok=koltukSayisi+yatakSayisi+dolapSayisi
    return donemBasiStok
def donSonuStok(satKoltukSayisi,satDolapSayisi,satYatakSayisi,alKoltukSayisi,alYatakSayisi,alDolapSayisi):
    global donemSonuStok
    donemSonuStok=(dolapSayisi-satDolapSayisi)+(yatakSayisi-satYatakSayisi)+(koltukSayisi-satKoltukSayisi)+alKoltukSayisi+alYatakSayisi+alDolapSayisi
    return donemSonuStok
def ortStok(donBasStok,donSonStok):
    ortalamaStok=(donemBasiStok+donemSonuStok)/2
    print('Ortalama stok:',ortalamaStok)

dolapSayisi=int(20)
yatakSayisi=int(30)
koltukSayisi=int(25)
print('Dolap sayınız:',dolapSayisi)
print('Yatak sayısı:',yatakSayisi)
print('Koltuk sayınız:',koltukSayisi)
donBasStok=donBasiStok(dolapSayisi,yatakSayisi,koltukSayisi)
print('Dönem başı stok:',donemBasiStok)
satKoltukSayisi=int(25)
satYatakSayisi=int(20)
satDolapSayisi=int(10)
print('Satılan koltuk sayısı:',satKoltukSayisi)
print('Satılan yatak sayısı:',satYatakSayisi)
print('Satılan dolap sayısı:',satDolapSayisi)
alKoltukSayisi=int(10)
alYatakSayisi=int(15)
alDolapSayisi=int(5)
print('Alınan koltuk sayısı:',alKoltukSayisi)
print('Alınan yatak sayısı:',alYatakSayisi)
print('Alınan dolap sayısı:',alDolapSayisi)
donSonStok=donSonuStok(satKoltukSayisi,satDolapSayisi,satYatakSayisi,alKoltukSayisi,alYatakSayisi,alDolapSayisi)
print('Dönem sonu stok:',donemSonuStok)
a=donBasiStok(dolapSayisi,yatakSayisi,koltukSayisi)
b=donSonuStok(satKoltukSayisi,satDolapSayisi,satYatakSayisi,alKoltukSayisi,alYatakSayisi,alDolapSayisi)
ortStok(a,b)
