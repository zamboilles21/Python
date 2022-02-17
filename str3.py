from os import system

system("cls")

szoveg = input("Irj be egy szöveget: ")

if len(szoveg) % 2 == 0:
    print(szoveg[len(szoveg) //2 - 1]+szoveg[len(szoveg)//2])
else:
    print(szoveg[len(szoveg)//2])