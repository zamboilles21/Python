from os import system

system("cls")

a=int(input("Irj be egy számot: "))
b=int(input("Irj be egy számot: "))
c=int(input("Irj be egy számot: "))

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("JA")
else:
    print("NO")