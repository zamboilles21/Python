from os import system

system("cls")

szamok = []
for i in range(3):
    szamok.append(int(input(f"{i+1} szám: ")))

print(f"A lista legkisebb elem:{min(szamok)}")
print(f"A lista legnagyobb elem:{max(szamok)}")