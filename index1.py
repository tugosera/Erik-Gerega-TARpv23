print("Tere! Olen sinu uus sõber - Python!")
print("Mis on sinu nimi?")
try:
    nimi=str(input())
except:
    ValueError
print(nimi, ", oi kui ilus nimi!" )
print(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
otvet=int(input())
if otvet==0:
    print("Kahju! See on väga kasulik info!")
    print()
elif otvet==1:
    pikkus=float(input("Sinu pikkus on => "))
    mass=float(input("sinu mass on => "))
    x=mass/(0.01*pikkus)**2
    index=round(x,1)
    print("! Sinu keha indeks on:", index)
    if index<16:
        print("Tervisele ohtlik alakaal")
    elif 16<=index<=19:
        print("Alakaal")
    elif 19<index<=25:
        print("Normaalkaal")
    elif 25<index<=30:
        print("Ülekaal")
    elif 30<index<=35:
        print("Rasvumine")
    elif 35<index<=40:
        print("Tugev rasvumine")
    elif 40<index:
        print("Tervisele ohtlik rasvumine")
    else:
        print("viga")







