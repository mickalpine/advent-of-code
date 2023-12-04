import logging
from typing import List

logger = logging.getLogger(__name__)


def lines_to_list(input) -> List:
    return [line for line in input.split("\n")]


def solution(lines) -> int:
    return sum([process_line(line) for line in lines])


def process_line(line):
    result = 1
    winning_nums, my_nums = parse_line(line)
    logger.debug(f"{winning_nums=}, {my_nums=}")

    matching_nums = set(winning_nums).intersection(my_nums)
    logger.debug(f"{matching_nums=}")

    if not matching_nums:
        return 0
    result = 2 ** (len(matching_nums) - 1)

    return result


def parse_line(line):
    winning_list, my_list = line.split(" | ")
    winning_list = winning_list.split(": ")[-1]
    winning_list = [x.strip() for x in winning_list.split()]

    my_list = [x.strip() for x in my_list.split()]

    return winning_list, my_list


def test_part1():
    example_input = r"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    example_input_list = lines_to_list(example_input)
    example_solution_lines = [8, 2, 2, 1, 0, 0]
    example_solution = 13

    solution_lines = [process_line(line) for line in example_input_list]
    logger.info(f"Got: {solution_lines=} Expected: {example_solution_lines=}")
    assert solution_lines == example_solution_lines

    result = solution(example_input_list)
    logger.info(f"Got: {result=} Expected: {example_solution=}")
    assert result == example_solution


if __name__ == "__main__":
    format = "%(levelname)s:%(message)s"
    logging.basicConfig(level=logging.INFO, format=format)

    with open("input.txt") as f:
        input = f.read().splitlines()

    logging.critical(f"Solution: {solution(input)}")
