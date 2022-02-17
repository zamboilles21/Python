from os import system

system("cls")

szam = int(input("Írj be egy számot: "))

if szam % 3 == 0 or szam % 5 == 0:
    print("Igen")
else:
    print("nem")
    