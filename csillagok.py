from os import system

system("cls")

szoveg=input("Adj meg egy szó: ")

s=" "

for x in szoveg:
    s+=x
    s+="*"
print(s[0:-1])