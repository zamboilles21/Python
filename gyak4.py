from os import system

system("cls")

a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))

if a + b == c or a + c == b or b + c == a:
    print("Egyenlő")
else:
    print("Nem egyenlő")  