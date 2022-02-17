from os import system

system("cls")

szam = int(input("Írj be egy egész számot: "))

isPrime = True

for _ in range(2, szam//2 + 1):
    if  szam %_ == 0:
        isPrime = False
        break

if isPrime:
    print(f"{szam} Prím")
else:
    print(f"{szam} nem Prím")

print(f"{szam} {}")

print("primoszto")

oszto = 2
valasz = f"{szam} = "
while szam > 1:
    if szam % oszto == 0:
        valasz += f"{oszto}"
        szam // = oszto:

print(valasz)