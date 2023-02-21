import random

class Cloth:
    def __init__(self, name, type, color, size, season):
        self.name = name #identifier
        self.type = type #up, down, feet, head
        self.season = season #winter, summer, autumn, spring
        self.color = color #Any
        self.size = size #fit, oversize, adjust


def getcomb(up, down, feet, head):
    return max(1, up) * max(1, down) * max(1, feet) * max(1, head)


def getoutfit(n, dicClothes, mask):
    key = random.randint(0, n - 1)
    if "up" in dicClothes[key].type:
        outfit[1] = dicClothes[key].name
        mask = mask | (1 << 1)
    elif "down" in dicClothes[key].type:
        outfit[2] = dicClothes[key].name
        mask = mask | (1 << 2)
    elif "head" in dicClothes[key].type:
        outfit[0] = dicClothes[key].name
        mask = mask | (1 << 0)
    elif "feet" in dicClothes[key].type:
        outfit[3] = dicClothes[key].name
        mask = mask | (1 << 3)
    else:
        print(dicClothes[key].type)
    print(key, mask)
    if mask >= 14:
        return
    else:
        getoutfit(n, dicClothes, mask)

print("number of clothes: ")

n = int(input())
dicClothes = {}
s = set(range(n))
dict.fromkeys(s)

up = 0
down = 0
head = 0
feet = 0
for i in range(n):
    name = input("Name of cloth #" + str(i + 1) + ": ")
    type = input("Type of cloth #" + str(i + 1) + ": ")
    if "up" in type:
        up += 1
    elif "down" in type:
        down += 1
    elif "head" in type:
        head += 1
    elif "feet" in type:
        feet += 1
    else:
        print("val: " + type)
    season = input("Season of cloth #" + str(i + 1) + ": ")
    color = input("Color of cloth #" + str(i + 1) + ": ")
    size = input("Size of cloth #" + str(i + 1) + ": ")
    cc = Cloth(name, type, color, size, season)
    dicClothes[i] = cc

comb = getcomb(up, down, head, feet)

print("You have " + str(comb) + "possibles. The best is:")

mask = 0
outfit = [[""] for i in range(n)]
getoutfit(n, dicClothes, mask)
print(str(outfit[0]) + ' - ' + str(outfit[1]) + ' - ' + str(outfit[2]) + ' - ' + str(outfit[3]))
"""
    4
    sombrero
    head
    winter
    red
    large
    playera naranja
    up
    winter   
    blue
    fit
    pantalones azules
    down
    summer
    orange
    fit
    zapatos viejos
    feet
    summer
    orange
    fit
"""