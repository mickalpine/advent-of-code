from typing import List
import logging

logger = logging.getLogger(__name__)

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


def parse_input(input) -> List:
    return [line for line in input.split("\n")]


def process_line(line):
    # print(f"line before: {line}")
    words_found = scan_line_words(line)
    if not words_found:
        left_pointer = scan_line(line, "left")
        right_pointer = scan_line(line, "right")
        return int(left_pointer + right_pointer)
    print(f"{words_found=} {line=}")

    first_word = min(words_found, key=words_found.get)
    print(f"first_word={first_word}")

    print(f"line before: {line}")
    line.replace(first_word, str(DIGITS[first_word]))
    print(f"line after: {line}")
    # process_line(line)
    # for k, v in words_found.items():
    #     line = line.replace(k, str(v))
    #
    return line


def scan_line(line, side):
    step = 1
    if side == "right":
        step = -1
    for i, char in enumerate(line[::step]):
        if char.isdigit():
            return char
    return ""


def scan_line_words(line):
    words_found = {}
    for k, v in DIGITS.items():
        word_start_index = line.find(k)
        if word_start_index != -1:
            words_found[k] = word_start_index

    # print(f"words_found: {words_found} in {line}")

    # print(f"line after: {line}")
    return words_found


def solution(lines) -> int:
    return sum([process_line(line) for line in lines])


def test_part2():
    example_input = r"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    example_solution_lines = [29, 83, 13, 24, 42, 14, 76]
    example_solution = 281

    example_input_list = parse_input(example_input)

    # for i, line in enumerate(example_input_list):
    # left_digit, right_digit = str(example_solution_lines[i])

    result = [process_line(line) for line in example_input_list]
    logging.debug(result)
    #     assert result.isdigit()
    #     assert result == left_digit
    #
    #     result = scan_line(line, "right")
    #     assert result.isdigit()
    #     assert result == right_digit
    #
    #     result = process_line(line)
    #     assert result == example_solution_lines[i]
    #
    # solution_lines = [process_line(line) for line in example_input_list]
    # assert solution_lines == example_solution_lines
    #
    # assert solution(example_input_list) == example_solution


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().splitlines()

    print(f"solution: {solution(input)}")
