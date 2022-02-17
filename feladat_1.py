from os import system
from random import randint
system("cls")

def kiir(a):
    for sor in a:
        for adat in sor:
            print(adat, end="")
    print()
matrix = []

n = int(input("Írj be egy N egész számot (1<=N<=10): "))

for i in range(n):
    lista = []
    for j in range(n):
        lista.append(randint(10,99))
    matrix.append(lista)

for sor in matrix:
    for adat in sor:
        print(adat, end="")
    print()

for i in range(n):
    matrix[i][i]=0
print()
kiir(matrix)
''' 
for sor in matrix:
    for adat in sor:
        print(adat, end="")
    print() '''
        
            
    