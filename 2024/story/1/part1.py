with open("data/part1.txt", "r") as f:
    input = f.read().split("\n")

instructions = []
for line in input:
    instr_dict = {}
    for instruction in line.split(" "):
        instr_dict[instruction[0]] = int(instruction[2:])
    instructions.append(instr_dict)


def eni(n: int, exp:int, mod: int) -> int:
    score = 1
    remainders = []
    for i in range(exp):
        score *= n
        remainder = score % mod
        remainders.insert(0, remainder)
    return int("".join(map(str, remainders)))

list_of_calls = []
for instruction in instructions:
    print(instruction)
    a = instruction['A']
    b = instruction['B']
    c = instruction['C']
    x = instruction['X']
    y = instruction['Y']
    z = instruction['Z']
    m = instruction['M']
    list_of_calls.append(eni(a, x, m) + eni(b, y, m) + eni(c, z, m))

print(max(list_of_calls))
    