# with open("example.txt", "r") as file:
with open("input.txt", "r") as file:
    input = file.read().splitlines()

cals_sum = 0
cals_list = []
for cals in input:
    if cals != "":
        cals_sum += int(cals)
    else:
        cals_list.append((cals_sum))
        cals_sum = 0
print(f"Part1: {max(cals_list)}")
print(f"Part2: {sum(sorted(cals_list)[-3:])}")
