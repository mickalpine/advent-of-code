from enum import Enum


with open("example.txt", "r") as file:
    # with open("input.txt", "r") as file:
    input = file.read().splitlines()


class OpponentThrow(Enum):
    A = 1
    B = 2
    C = 3


class PlayerThrow(Enum):
    X = 1
    Y = 2
    Z = 3


class Match(Enum):
    loss = 0
    draw = 3
    win = 6


class RoundEnd(Enum):
    X = "loss"
    Y = "draw"
    Z = "win"


player_winner_dict = {
    OpponentThrow.A: PlayerThrow.Y,
    OpponentThrow.B: PlayerThrow.Z,
    OpponentThrow.C: PlayerThrow.X,
}

player_loser_dict = {
    OpponentThrow.A: PlayerThrow.Z,
    OpponentThrow.B: PlayerThrow.X,
    OpponentThrow.C: PlayerThrow.Y,
}


def get_round_points(opponent_throw: OpponentThrow, player_throw: PlayerThrow) -> int:
    if opponent_throw.value == player_throw.value:
        # print(f"tie {player_throw.value=}, {opponent_throw.value=}")
        return Match.draw.value

    if player_throw.value - 1 == opponent_throw.value:
        # print(f"player won {player_throw.value=}, {opponent_throw.value=}")
        return Match.win.value

    if player_throw.value == 1 and opponent_throw.value == 3:
        # print(f"player won {player_throw.value=}, {opponent_throw.value=}")
        return Match.win.value
    # print(f"lost {player_throw.value=}, {opponent_throw.value=}")
    return Match.loss.value


def pick_shape(opponent_throw: OpponentThrow, round_ends: RoundEnd):
    if round_ends.value == "draw":
        # print(f"{round_ends.value=}: {opponent_throw=} {opponent_throw.value}")
        return opponent_throw.value + Match.draw.value
    if round_ends.value == "win":
        # print(
        #     f"{round_ends.value=}: {opponent_throw=} {player_winner_dict[opponent_throw]=}"
        # )
        return player_winner_dict[opponent_throw].value + Match.win.value

    # print(
    #     f"{round_ends.value=}: {opponent_throw=} {player_loser_dict[opponent_throw]=}"
    # )
    return player_loser_dict[opponent_throw].value + Match.loss.value


def part1(input: list[str]) -> int:
    player_score = []
    for round in input:
        opponent, _, player = round
        opponent_throw = OpponentThrow[opponent]
        player_throw = PlayerThrow[player]

        winner_points = get_round_points(opponent_throw, player_throw)
        throw_points = player_throw.value
        round_score = winner_points + throw_points
        # print(f"{round_score=}")
        player_score.append(round_score)
    return sum(player_score)


def part2(input: list[str]) -> int:
    player_score = []
    for round in input:
        opponent, _, ending = round
        opponent_throw = OpponentThrow[f"{opponent}"]
        round_ends = RoundEnd[f"{ending}"]

        round_score = pick_shape(opponent_throw, round_ends)
        # print(f"{round_score=}")
        player_score.append(round_score)
    return sum(player_score)


if __name__ == "__main__":
    print(f"{part1(input)=}")
    print(f"{part2(input)=}")
