from os import system

system("cls")

szo = input("Irj be egy szót: ")

if len(szo) % 2 == 0:
    print(szo[len(szo) //2 - 1]+szo[len(szo)//2-1], end="")
