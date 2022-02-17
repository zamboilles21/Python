from os import system

system("cls")

class dolgozok:
    def __init__(self, nev, beosztas, telefon, alapber):
        self.nev = nev
        self.beosztas = beosztas
        self.telefon=telefon
        self.alapber=alapber
    def __str__(self):
        return f"{self.nev} {self.beosztas} {self.telefon} {self.alapber}"
adatok_lista=[]
for i in range(3):
    nev=input('Kérem a dolgozó nevét: ')
    beosztas=input('Kérem a dolgozó beosztását: ')
    telefon=input('Kérem a dolgozó telefonszámát!')
    alapber=int(input('Kérem a dolgozó alapbérét!'))

    egydolgozo=dolgozok(nev,beosztas,telefon,alapber)
    adatok_lista.append(egydolgozo)
    print(adatok_lista[i])

maxi=adatok_lista[0]

for i in adatok_lista:
    if i.alapber>maxi.alapber:
        maxi=i
print(maxi)

with open('magas.txt','w',encoding='utf8') as cel:
    print('Legmagasabb bér: ',maxi.alapber,'A dolgozó neve: ', maxi.nev, file=cel)
    




