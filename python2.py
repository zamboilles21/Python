"""
szam = int(input("Írd be egy egész számot: "))
if(szam % 2 == 0):
    print(str(szam)+"páros")
else:
    print(f"{szam} páratlan")
"""
print("Hello World", end="")
print("Hello World")

szam = int(input("Írd be egy egész számot: "))
print(f"{szam} osztoi: ")
print("1; ", end="")

n = 2
while n <= szam/2:
    if szam % n == 0:
        print(f"{n}; ")
    n += 1
print(szam)
