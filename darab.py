from os import system

system("cls")

db = int(input("Írj be egy egész számot: "))

szamok = []

for i in range(db):
    szamok[i]=int(input(f"{i+1}. szám: "))


for szam in szamok:
    if szam % 2 == 0:
        print(f"A(z){szamok.index(szam)}. szám páros: {szam}")