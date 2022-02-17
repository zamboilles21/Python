from os import system
from random import randint
from fuggvenyek import *

system("cls")

matrix = []

for i in range(8):
    sor=[]
    for j in range(8):
        sor.append(randint(10, 99))
    matrix.append(sor)

kiir(matrix)

min_lista, max_lista = [], []

for i in range(8):
    min_lista.append(min(matrix[i]))
    max_lista.append(max(matrix[i]))

min = min(min_lista)
max = max(max_lista)
print(f"a mátrix legkisebb eleme: {min}, Legnagyobb: {max}.")    


    