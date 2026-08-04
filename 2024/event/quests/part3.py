def potion_check(enemy: str) -> int:
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
            case _:
                return 0

with open("data/part3.txt", "r") as f:
    input = f.read()

potions = 0
extra = 2    
for i in range(0, len(input), 3):
    enemy1 = input[i]
    enemy2 = input[i + 1]
    enemy3 = input[i + 2]
    first = potion_check(enemy1)
    second = potion_check(enemy2)
    third = potion_check(enemy3)
    enemy_list = [enemy1, enemy2, enemy3]
    
    num_enemies = 0
    for enemy in enemy_list:
        if enemy != "x":
            num_enemies += 1
            
    num_unique = len(set(enemy_list))
    increment = (first  + second + third)
    if num_enemies == 2:
        increment += 2
    elif num_enemies == 3:
        increment += 6
    potions += increment
    
    
print(potions)
    

