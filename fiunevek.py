from os import system

system("cls")

adatok=[]

with open('fiunevek.txt','r',encoding='utf8') as r:
    for sor in r:
        adatok.append(sor)
print(f"{len(adatok)} van a listában")


