with open("data/part2.txt", "r") as f:
    input = f.read().split("\n")

instructions = []
for line in input:
    instr_dict = {}
    for instruction in line.split(" "):
        instr_dict[instruction[0]] = int(instruction[2:])
    instructions.append(instr_dict)

def eni(n: int, exp:int, mod: int) -> int:
    first_power = max(1, exp - 4)
    remainders = [
        pow(n, exp, mod) 
        for exp in range(exp, first_power - 1, -1)
    ]
    return int("".join(map(str, remainders[:5])))


best_score = max(
    eni(row["A"], row["X"], row["M"])
    + eni(row["B"], row["Y"], row["M"])
    + eni(row["C"], row["Z"], row["M"])
    for row in instructions
)

print(best_score)
    