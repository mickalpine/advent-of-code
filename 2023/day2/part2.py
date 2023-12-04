import logging
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List

logger = logging.getLogger(__name__)


def lines_to_list(input) -> List:
    return [line for line in input.split("\n")]


def solution(lines) -> int:
    return sum([process_line(line) for line in lines])


def process_line(line):
    game = Game()
    game.parse_game(line)
    logger.info(f"{game=}")

    minimums = game.get_minimum_colors()
    minimums_cubed = 1
    for v in minimums.values():
        minimums_cubed *= v

    return minimums_cubed


class Color(Enum):
    red = "red"
    green = "green"
    blue = "blue"

    def __repr__(self) -> str:
        return self.value


@dataclass
class Draw:
    colors: Dict[Color, int]


@dataclass
class Game:
    id: int = field(default=0)
    draws: List[Draw] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"{self.id} {self.draws}"

    def parse_game(self, line):
        id, draws = line.split(": ")
        self.id = int(id.split()[-1])
        self.parse_draws(draws)

    def parse_draws(self, line):
        line = [draw for draw in line.split("; ")]

        for draw in line:
            draw = [cubes for cubes in draw.split(", ")]
            draw = Draw(
                {
                    Color(color): int(number)
                    for number, color in [c.split() for c in draw]
                }
            )
            logger.debug(f"adding {draw=} to {self.draws}")
            self.draws.append(draw)

    def is_valid(self) -> bool:
        VALID_COLOR_MAXIMUM = {Color.red: 12, Color.green: 13, Color.blue: 14}
        return all(
            num <= VALID_COLOR_MAXIMUM[color]
            for draw in self.draws
            for color, num in draw.colors.items()
        )

    def get_minimum_colors(self):
        minimums = defaultdict(int)
        for draw in self.draws:
            for color, num in draw.colors.items():
                minimums[color] = max(minimums[color], num)
        return minimums


def test_part1():
    example_input = r"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    example_input_list = lines_to_list(example_input)
    example_solution_lines = [48, 12, 1560, 630, 36]
    example_solution = 2286

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
