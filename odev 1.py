x=int(input("finansmanGelir:"))
y=int(input("pazarGelir:"))
z=int(input("kiraGelir:"))
gelir=x+y+z
print("Gelir",gelir)
a=int(input("ucret:"))
b=int(input("finansmanGider:"))
c=int(input("pazarGider:"))
d=int(input("kiraGider:"))
e=int(input("muhasebeGider"))
gider=a+b+c+d+e
print("Gider",gider)
kar=gelir-gider
if kar>1000:
    print("İşletme karlıdır.")
else:
    print("İşletme zararlıdır.")

