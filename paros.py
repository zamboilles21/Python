from os import system

system("cls")


szam1=int(input("Irj be egy számot: "))
szam2=int(input("Irj be egy számot: "))

for i in range(szam1,szam2):
    if i % 2 ==0:
        print(f"{i}, ", end="")