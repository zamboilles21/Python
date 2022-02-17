from os import system

system("cls")

szam = int(input("Irj be egy egész számot: "))

print(f"{szam} = ", end="")
while szam % 2 == 0:
    print("2*")
    szam //=2
print(szam)