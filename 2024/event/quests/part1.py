with open("data/part1.txt", "r") as f:
    input = f.read()

potions = 0    
for char in input:
    match char:
        case "A":
            continue
        case "B":
            potions += 1
        case "C":
            potions += 3
        case _:
            print(char)

print(potions)            