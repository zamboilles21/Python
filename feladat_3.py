from os import system
from fuggvenyek import *

system("cls")

n = int(input("Írj be egy N egész számot (1<=N<=10): "))

matrix = maxfeltolto(n, 10, 99)
kiir(matrix)
print()
matrix[0], matrix[-1] = matrix[-1], matrix[0]
kiir(matrix)