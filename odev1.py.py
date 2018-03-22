satisMiktari=500
birimSatisFiyati=20
ciro=5000
i=0
while (ciro<=500000):
    ciro=ciro+(satisMiktari*birimSatisFiyati)
    satisMiktari=satisMiktari+200
    birimSatisFiyati=birimSatisFiyati+10
    i=i+1
print("500.000'den fazla kar",i,".ayda tamamlanmıştır.")
