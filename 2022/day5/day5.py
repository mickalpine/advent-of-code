# with open("example.txt", "r") as f:
with open("input.txt", "r") as f:
    input = f.read().splitlines()


def create_crates(input):
    crates: list[str] = []
    for line in iter(input):
        if line != "":
            crates.append(line)
        else:
            break
    return crates


def create_instructions(input):
    crates = create_crates(input)
    instructions = input[len(crates) + 1 :]
    # print(instructions)
    return instructions


def create_column_dict(input):
    crates = create_crates(input)
    column = 1
    column_dict = {}
    # print(len(crates))
    # print(f"{len(crates) - 1=}")
    for line in range(0, len(crates)):
        crates_list = []
        for line in crates:
            # print(line[column])
            if str.isalnum(line[column]):
                crates_list.append(line[column])
        column_dict[crates_list.pop()] = crates_list
        column += 4
    return column_dict


def part1(input) -> str:
    instructions = create_instructions(input)
    column_dict = create_column_dict(input)
    for line in instructions:
        # print(line.split())
        _, move_qty, _, from_col, _, to_col = line.split()

        # print(f"{move_qty=}, {from_col=}, {to_col=}")
        # print(f"BEFORE FROM: {column_dict[from_col]=}")
        # print(f"BEFORE TO: {column_dict[to_col]=}")
        for crate in range(0, int(move_qty)):
            column_dict[to_col].insert(0, column_dict[from_col].pop(0))
        # print(f"AFTER FROM: {column_dict[from_col]=}")
        # print(f"AFTER TO: {column_dict[to_col]=}")

    message = [stack[0] for stack in column_dict.values()]
    message = "".join(message)
    return message


def part2(input) -> str:
    instructions = create_instructions(input)
    column_dict = create_column_dict(input)

    for line in instructions:
        _, move_qty, _, from_col, _, to_col = line.split()
        qty = int(move_qty) - 1

        for crate in range(0, int(move_qty)):
            column_dict[to_col].insert(0, column_dict[from_col].pop(qty))
            qty -= 1

    message = [stack[0] for stack in column_dict.values()]
    message = "".join(message)
    return message


if __name__ == "__main__":
    print(f"Part1: {part1(input)}")
    print(f"Part2: {part2(input)}")
