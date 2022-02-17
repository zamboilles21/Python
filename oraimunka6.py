from os import system

system("cls")

szam = int(input("Irj be egy egész számot: "))
szamok=[]

for i in range(szam):
    szamok.append(int(input(f"{i+1}. szám: ")))

max = max(szamok)
min = min(szamok)
print(f"{max} + {min} = {max - min}")
