from os import system
from random import randint

system('cls')
osszeg = 0
min = 30
max = 1
#szamok = []
for i in range(15):
    szam = randint(1, 30)
    osszeg += szam
    print(szam) if i == 14 else print(f"{szam}, ",end="")
    """
    if szam < min:
        min = szam
    if  szam > max
        max = szam
        """
    """
    if i == 14:
        print(szam)
    else:
        print(f"{szam}, ", end="")
"""
#osszegzes

#for szam in szamok:
    #osszeg += szam
print(f"\nA tomb elemeinek osszege: {osszeg}")