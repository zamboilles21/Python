from os import system

system("cls")

interv=[]
interv.append(int(input("Irj be egy számot")))
interv.append(int(input("Irj be egy számot")))

for i in range(min(interv, max(interv)+1)):
    if i % 2 ==0:
        print(f"{i} ", end="")