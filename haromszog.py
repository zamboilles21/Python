from os import system

system("cls")

szam = int(input("Írj be egy egész számot: "))

"""
for i in range(szam):
    for j in range(i * 2+1):
        print ("*", end="")
    print()
"""
for_ in range(szam):
    print("*" * (_ *2+1))     