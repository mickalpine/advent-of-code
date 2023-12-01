from typing import List
import logging

logger = logging.getLogger(__name__)


def parse_input(input) -> List:
    return [line for line in input.split("\n")]


def process_line(line):
    left_pointer = scan_line(line, "left")
    right_pointer = scan_line(line, "right")

    # if line.index(left_pointer) == line.rindex(right_pointer):
    #     return int(left_pointer)

    return int(left_pointer + right_pointer)


def scan_line(line, side):
    step = 1
    if side == "right":
        step = -1
    for i, char in enumerate(line[::step]):
        if char.isdigit():
            return char
    return ""


def solution(lines) -> int:
    return sum([process_line(line) for line in lines])


def test_part1():
    example_input = r"""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    example_solution_lines = [12, 38, 15, 77]
    example_solution = 142

    example_input_list = parse_input(example_input)

    for i, line in enumerate(example_input_list):
        left_digit, right_digit = str(example_solution_lines[i])

        result = scan_line(line, "left")
        assert result.isdigit()
        assert result == left_digit

        result = scan_line(line, "right")
        assert result.isdigit()
        assert result == right_digit

        result = process_line(line)
        assert result == example_solution_lines[i]

    solution_lines = [process_line(line) for line in example_input_list]
    assert solution_lines == example_solution_lines

    assert solution(example_input_list) == example_solution


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().splitlines()

    print(f"solution: {solution(input)}")
