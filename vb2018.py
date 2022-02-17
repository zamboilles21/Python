from oszt import Stadion
from os import system

system("cls")

#2.feladat
stadionok = []
with open("vb2018.txt", encoding='utf8') as f:
    next(f)
    for sor in f:
        stadionok.append(Stadion(sor))

#3.feladat

print(f"3.feladat: stadionok száma: {len(stadionok)}")

# 4.feladat
#min = stadionok[0].ferohely
min = 0
for i in range(len(stadionok)):
    if stadionok[i].ferohely < stadionok[min].ferohely:
        min = i

print("A legkevesebb férőhely:")
print(f"Város: {stadionok[min].varos}")
print(f"Stadion neve:{stadionok[min].nev1}")
print(f"Férőhely: {stadionok[min].ferohely}")