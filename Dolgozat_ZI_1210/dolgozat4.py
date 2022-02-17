from os import system
from random import randint
system("cls")

for i in range(50):
    szam = randint(1, 9)
    print(szam) if i == 49 else print(f"{szam}, ",end="")

szamsz = int(input("Adj meg egy 1-9 közötti számot: "))

#if szamsz == szam:
    #print(f"{szam}")
    
