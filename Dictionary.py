class cloth:
    def __init__(self, type, color, size):
        self.type = type #up, down, feet, head
        self.color = color #Any
        self.size = size #fit, large, adjust


def getcomb(up, down, feet, head):
    return max(1, up) * max(1, down) * max(1, feet) * max(1, head)


print(getcomb(3, 2, 0, 0))
print("number of clothes: ")

n = int(input())
dicClothes = {}
s = set(range(n))
dict.fromkeys(s)

up: int = 0
down: int = 0
head: int = 0
feet: int = 0
for i in range(n):
    print("Type of cloth #" + str(i + 1) + ": ")
    type = input()
    if type == "up":
        up+=1
    if type == "down":
        down += 1
    if type == "head" :
        head += 1
    if type == "feet" :
        feet += 1
    print("Color of cloth #" + str(i + 1) + ": ")
    color = input()
    print("Size of cloth #" + str(i + 1) + ": ")
    size = input()
    cc = cloth(type, color, size)
    dicClothes[i] = cc

comb = getcomb(up, down, head, feet)

print("You have " + str(comb) + "possibles. The best are:")

"""
    4
    
    up
    
    red
    
    large
    
    up
    
    blue
    
    fit
    
    down
    
    orange
    
    fit
    
    down
    
    orange
    
    fit
"""