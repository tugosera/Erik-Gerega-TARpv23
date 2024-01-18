print("Tere! Olen sinu uus sõber - Python!")
print("Mis on sinu nimi?")
nimi=input()
print(nimi, ", oi kui ilus nimi!" )
print(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
otvet=int(input())
if otvet==0 :
    print("Kahju! See on väga kasulik info!")
    print()
elif otvet==1 :
    print("Sinu pikkus on =>")
    pikkus=int(input())
    print("sinu mass on =>")
    mass=float(input())
    x=mass/(0.01*pikkus)**2
    index = round(x,1)
    print("! Sinu keha indeks on:", index)

