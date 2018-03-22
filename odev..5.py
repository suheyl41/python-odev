gunlukUretilen=200
gunlukDefoluUrun=0
toplamDefUrun=0
i=0
while(gunlukDefoluUrun<=gunlukUretilen*0.20):
    gunlukDefoluUrun=int(input("Günlük Defolu Ürün Miktarı:"))
    toplamDefUrun=toplamDefUrun+gunlukDefoluUrun
    i=i+1
    if(gunlukDefoluUrun>gunlukUretilen*0.20):
        print("Defolu Ürün Sayısı Limiti Aştı")
        break

    print(i,"Günlük","Defolu Ürün Sayısı:",toplamDefUrun)                         
