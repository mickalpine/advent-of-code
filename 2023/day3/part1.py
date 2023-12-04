import logging
import os
from collections import namedtuple
from dataclasses import dataclass, field
from itertools import groupby
from string import digits as DIGITS
from typing import List, Optional

filename = os.path.splitext(os.path.basename(__file__))[0]
logger = logging.getLogger(filename)


def lines_to_list(input) -> List:
    return [line for line in input.split("\n")]


def solution(lines) -> int:
    return sum(process_lines(lines))  # type: ignore
    # return sum([process_line(line) for line in lines])  # type: ignore


SYMBOLS = ["*", "#", "+", "$"]

Number = namedtuple("Number", ["y", "x", "value"])
Symbol = namedtuple("Symbol", ["y", "x", "value"])


@dataclass
class Part:
    numbers: List[Number] = field(default_factory=list)
    _value: str = ""

    @property
    def value(self) -> int:
        return int(self._value) if self._value else 0


def process_line(line, y):
    symbols = []
    numbers = []
    for x, char in enumerate(line):
        if char in DIGITS:
            numbers.append(Number(y, x, char))
            logger.debug(f"{char=} at index {x}")
        if char in SYMBOLS:
            symbols.append(Symbol(y, x, char))
            logger.debug(f"{char=} at index {x}")

    logger.debug(f"{symbols=} {numbers=}")
    return symbols, numbers


def process_lines(lines):
    symbols = []
    numbers = []
    valid_part_numers = []
    for y, line in enumerate(lines):
        logger.info(f"{'='*80}\n{line=}")
        _symbols, _numbers = process_line(line, y)
        symbols += _symbols
        numbers += _numbers

    # logger.info(f"{'='*80}\n{numbers=}")
    logger.info(f"{'='*80}")
    parts = process_numbers(numbers)
    logger.info(f"{[part.value for part in parts]}")
    # logger.info(f"{parts=}")

    return valid_part_numers
    # logger.info(f"{symbols=} {numbers=}")


def process_numbers(numbers):
    """Return a list of parts"""
    result = []
    current_part = Part()

    for num in numbers:
        logger.debug(f"{current_part} {num=}")
        if current_part is None or num.x != current_part.numbers[-1].x + 1:
            # if current_part.numbers and num.x != current_part.numbers[-1].x + 1:
            # Start a new part
            current_part = Part(numbers=[num], _value=num.value)
            result.append(current_part)
        else:
            # Add to the current part
            current_part.numbers.append(num)
            current_part._value = current_part._value + num.value

    return result


def test_part1():
    example_input = r"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    example_input_list = lines_to_list(example_input)
    example_solution_lines = [467, 35, 633, 617, 592, 755, 664, 598]
    example_solution = 4361

    assert sum(example_solution_lines) == example_solution

    # solution_lines = [
    #     process_line(line, y) for y, line in enumerate(example_input_list)
    # ]
    # logger.info(f"Got: {solution_lines=} Expected: {example_solution_lines=}")
    # assert solution_lines == example_solution_lines

    result = solution(example_input_list)
    logger.info(f"Got: {result=} Expected: {example_solution=}")
    assert result == example_solution


if __name__ == "__main__":
    format = "%(levelname)s:%(message)s"
    logging.basicConfig(level=logging.DEBUG, format=format)

    with open("input.txt") as f:
        input = f.read().splitlines()

    logging.critical(f"Solution: {solution(input)}")
