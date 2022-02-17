from os import system

system("cls")

class Epulet:
    def __init__(self, nev, varos, orszag, magassag, emelet, epulz):
        self.nev=nev
        self.varos = varos
        self.orszag=orszag
        self.magassag=magassag
        self.emelet=emelet
        self.epulz=epulz

f = open("legmagasabb.txt", "r", encoding="utf8")
print(f.readline())

line_count=0
for i in f:
    if i != "\n":
        line_count += 1
f.close()

print("Épületek száma: ",line_count)

#for i in Epulet:
if self.magassag == self.magassag.max():
    print("Név: ",self.nev)
    print("Város: ",self.varos)
    print("Ország: " ,self.orszag)
    print("Magassága: ",self.magassag)
    print("Emeletek száma: " ,self.emelet)
    print("Ekkor épült: ",self.epult)


if self.orszag == "Olaszország":
    print("Van")
else:
    print("Nincs")
