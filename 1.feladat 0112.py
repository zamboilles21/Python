from os import system

system("cls")

szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy masik számot: "))

if szam1 > szam2:
    print(szam1,"nagyobb", szam2, "Kisebb")
elif szam1 == szam2:
    print("Egyenlő")
else:
    print(szam2,"nagyobb", szam1, "Kisebb")    
