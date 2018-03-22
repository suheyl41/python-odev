calisan=50
yevmiye=90
aylikMesai=0
haftalikMaas=630
aylikMaas=0
while aylikMesai<=22:
    haftalikMesai=int(input("Haftalık mesai:"))
    aylikMesai=haftalikMesai*4
    haftalikMaas=haftalikMaas+(haftalikMesai*yevmiye*0.10)
    aylikMaas=aylikMaas+haftalikMaas*4
    print("Aylik maas",aylikMaas)
else:
    print("Aylik mesai 22 saatten fazla olamaz")
