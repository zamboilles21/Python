from os import system

system("cls")
szo=input("Írj egy szót: ")
tabu=input("Irj be egy betut: ")

for betu in szo:
    if betu != tabu.lower():
        print(betu, end="")