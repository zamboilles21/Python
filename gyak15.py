from os import system

system("cls")

def matrix(oszlop, sor):
    for i in range(sor):
        for j in range(oszlop):
            print("*",end="")
        print()

sor = int(input("Sorok: "))
oszlop = int(input("oszlop: "))
matrix(oszlop, sor)