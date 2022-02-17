from os import system

system("cls")

nev = input("Irjon be egy nevet: ")

f=open('adatok1.txt', 'a')
f.write(nev)
f.close()