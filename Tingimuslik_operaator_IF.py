#1
nimi=input("Mis on sinu nimi?")
if nimi=="Juku":
    print("läheme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
       pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet)#ilus ja õige vastus! "Vale vanus"  või "On vaja osta...."

else:
    print("Ma ootan Jukut")

#2
nimi_üks= input("Mis on sinu nimi?")
nimi_kaks=input("Mis on sinu nimi?")
if nimi_üks == nimi_kaks:
    print("Samad nimed")
else:
    print("Täna " +nimi_üks+ " ja " +nimi_kaks+ " naabrid pingil ")

#3
print("Tere!")
pikkus=float(input("Mis on teie seinte pikkus?")) #первая сторона длинее (длина)
laius=float(input("Mis on teie seinte laius?")) #вторая сторона меньше чем первая (ширина)
põranda_pindala = pikkus * laius
print("Põranda pindala: " , põranda_pindala, "ruutmeetri")
remont=input("Kas soovite remonti teha? Jah, Ei =>")
if remont == "Jah" :
        hind=float(input("Kui palju see ruutmeeter maksab?: "))
        summa=hind*põranda_pindala
        print("Remondi hind:" , summa, "eurot")
else:
        print("Ma ei vaja remonti")

#4
from random import *
hind =randint(0,1000)
hind=float(input("Mis hind on? "))
if hind >=700:
    soodushind=hind*0.3
    print("Toode maksab" ,soodushind , "eurot")
else:
    print("Toode ilma allahindluseta")

#5
temperatuuri=float(input("Mis su temperatuur on?  "))
if temperatuuri>18:
    print("Temperatuur üle 18 kraadi")
else:
    print("Temperatuur mitte üle 18 kraadi")
    print("See on talvel soovitatav temperatuur")

#6
pikk=float(input("Kui pikk sa oled?  "))
if pikk<=160:
    print("Sul on madal kasv")
elif 160<pikk<=185:
    print("Sa oled keskmist kasvu")
elif 185<pikk<=220:
    print("Sa oled pikka kasvu")
else:
    print("Viga")

#7
pikk=float(input("Kui pikk sa oled?  "))
sugu=input("Mis soost sa oled? (naine või mees)")
if sugu =="naine":
    if pikk<=160:
        print("Sa oled madal naine")
    elif 160<pikk<=185:
        print("Sa oled keskmist kasvu naine")
    else :
       print("Sa oled pikk naine")
if sugu =="mees":
    if pikk<=160:
        print("Sa oled madal mees")
    elif 160<pikk<=185:
        print("Sa oled keskmist kasvu mees")
    elif 185<pikk<=220:
        print("Sa oled pikk mees") 
else:   
    print("Viga")

#8.1
from random import *
from datetime import *
arve_nr=date.today()#datetime.now()
print(arve_nr)
tsekk="Arve:  "+str(arve_nr)+"\nToode Hind Kogus Summa\n" 
summa=0

toode="Piim"
hind=randint(50,150)/100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu? "))
    tsekk+=mitu*hind
    summa+=mitu*hind
toode="Leib"
hind=randint(90,300)/100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu? "))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu? "))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("Makssa "+str(summa)))
if raha==summa:
    print("Tänan ostu eest!")
elif raha>summa:
    print("Tänan ostu eest! Tagasi "+str(raha-summa))

#8.2
from random import *
from datetime import *
arve_nr=date.today()#datetime.now()
print(arve_nr)
tsekk="Arve:  "+str(arve_nr)+"\nToode Hind Kogus Summa\n" 
summa=0
for toode in["Piim", "Leib", "Koom"]:
    hind=randint(50,150)/100
    v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu? "))
        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while True:
    raha=float(input("Maksa "+ str(summa)+"\n"))
    if raha==summa:
        print("Tänan ostu eest!")
        break
    elif raha>summa:
        print("Tänan ostu eest! Tagasi "+str(raha-summa))
        break
    else:
        summa=raha
        print("Maksa veel"+str(summa))



#9 
a=float(input("Sisenege küljele: "))
b=float(input("Sisenege küljele: "))
if a==b:
    print("See on ruut")
else:
    print("See ei ole ruut")

#10
from math import *
number=float(input("Sisestage number: "))
number1=float(input("Sisestage number: "))
märgid=input("Mida sa teha tahad? (Jah või Ei)")
if märgid=="Jah":
    operatsioonid=input("Valige toiming (+, -, /, *)")
    if operatsioonid=="+":
        tulemus=number+number1
        print("Lisamise tulemus: " +str(tulemus))
        if operatsioonid=="-":
            tulemus1=number-number1
            print("Tulemuse lahutamine: " +str(tulemus1))
            if operatsioonid=="/":
                tulemus2=number/number1
                print("Tulemuste jaotus: " +str(tulemus2))
            else:
                print("Nulliga jagada ei saa!")
        elif operatsioonid=="*":
                tulemus3=number*number1
                print("Korrutamise tulemus: " +str(tulemus3))
        else:
            print("Te ei saa nulliga korrutada!")
else:
    print("Viga")


#11
from datetime import*
from random import*
ta=date.today().year
sp=date(int(input("Sünniaasta: ")),int(input("Sümmikku: ")), int(input("Sünniäev: "))).year
if (ta-sp)%5==0:
    print("Juubell")
else:
    print("Tavaline sünnipäev")


#12
hind=float(input("Sisesta hind: "))
if hind<=10:
    allahindlust=hind*0.1
    print("Koguhind " +str(allahindlust)+ " eurot")
elif hind>=10:
    allahindlust1=hind*0.2
    print("Koguhind " +str(allahindlust1)+ " eurot")


#13
korrus=input("Kas sa oled mees või naine?")
if korrus=="mees":
    vanus=int(input("Palun märkige oma vanus "))
    if vanus>=16 and vanus<18:
        print("Sa sobid meie meeskonda!")
    else:
        print("Kahjuks sa ei sobi meie meeskonda!")
elif korrus=="naine":
    print("Kahjuks, otsime ainult mehi")
else:
     print("Viga")


#14
from datetime import*
from random import*
maht=int(input("Bussi maht: "))
i=int(input("Inimeste arv: "))
ba=round(i/maht) #2,3->2
if i%maht!=0:
    ba+=1
vb=i%maht
print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))


