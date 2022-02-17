from os import system

system("cls")

x=int(input("Elért pontszám (0-100): "))

if x <= 0 and x < 50:
    print("1")
elif 50 <= x and x < 60:
    print("2")
elif 60 <= x and x < 70:
    print("3")
elif 70 <= x and x < 85:
    print("4")
elif 85 <= x and x < 100:
    print("5")
else:
    print("Hibás")