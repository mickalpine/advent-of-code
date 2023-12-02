import logging
from typing import List

logger = logging.getLogger(__name__)


def lines_to_list(input) -> List:
    return [line for line in input.split("\n")]


def solution(lines) -> int:
    return sum([process_line(line) for line in lines])


def process_line(line):
    result = scan_line(line)
    logger.debug(f"{result=}")
    return result


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def scan_left_to_right(line):
    """
    Start at the beginning of a line and work forwards
    Check if the first character is a digit
    If not a digit, check if the line starts with a word in DIGITS
    If not, look at the next character to the end of the line
    """
    index = 0
    digit = ""

    logger.debug(f"Scanning left to right: {line=}")
    # starting from left to right
    while index < len(line) and not digit:
        text = line[index:]
        if text[0].isdigit():
            digit = str(text[0])
            logger.debug(f"Found {digit=} for {line=}")
            break
        else:
            for word in DIGITS:
                if text.startswith(word):
                    digit = str(DIGITS[word])
                    logger.debug(f"Found {digit=} for {word=} in {line=}")
                    break
        index += 1
    return digit


def scan_right_to_left(line):
    """
    Start at the end of a line and work backwards
    Check if the last character is a digit
    If not a digit, check if the line ends with a word in DIGITS
    If not, reduce the line by 1 character and look at remaining characters
    """
    index = len(line)
    digit = ""

    logger.debug(f"Scanning right to left: {line=}")
    while index >= 0 and not digit:
        logger.debug(f"{index=} at start")
        text = line[:index]
        logger.debug(f"{text=}")
        if text[-1].isdigit():
            digit = str(text[-1])
            logger.debug(f"Found {digit=} for {line=}")
            return digit
        else:
            for word in DIGITS:
                if text.endswith(word):
                    digit = str(DIGITS[word])
                    logger.debug(f"Found {digit=} for {word=} in {line=}")
                    return digit
        index -= 1
        logger.debug(f"{index=} at end")


def scan_line(line):
    left_digit = scan_left_to_right(line)
    right_digit = scan_right_to_left(line)

    return int(f"{left_digit}{right_digit}")


def test_part2():
    example_input = r"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    example_input_list = lines_to_list(example_input)
    example_solution_lines = [29, 83, 13, 24, 42, 14, 76]
    example_solution = 281

    solution_lines = [process_line(line) for line in example_input_list]
    logging.info(f"Got: {solution_lines=} Expected: {example_solution_lines=}")
    assert solution_lines == example_solution_lines

    result = solution(example_input_list)
    logging.info(f"Got: {result=} Expected: {example_solution=}")
    assert result == example_solution


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().splitlines()

    logging.critical(f"Solution: {solution(input)}")
