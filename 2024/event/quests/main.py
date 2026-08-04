def potion_check(enemy):
    match enemy:
            case "A":
                return 0
            case "B":
                return  1
            case "C":
                return  3
            case "D":
                return 5
            case "x":
                return 0

with open("data/part2.txt", "r") as f:
    input = f.read()

potions = 0
extra = 2    
for i in range(0, len(input), 2):
    enemy1 = input[i]
    enemy2 = input[i + 1]
    first = potion_check(enemy1)
    second = potion_check(enemy2)
    
    if enemy1 == "x" or enemy2 == "x":
        extra = 0
    else:
        extra = 2
    
    potions = potions + first + second + extra
    
print(potions)
    

