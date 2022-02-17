from os import system
from random import randint

def kiir(a):
    for sor in a:
        for adat in sor:
            print(adat, end="")
    print()

def maxfeltolto(n=8, min=10, max=99):
    matrix=[]
    for i in range(n):
        lista = []
        for j in range(n):
            lista.append(randint(min, max))
        matrix.append(lista)
    return matrix