# python 3.8

import itertools
import random
from game_of_war import *


scores = {
    "win_a": 0,
    "win_b": 0,
    "draw_move_limit": 0,
    "draw_no_cards": 0,
    "avg_moves": 0,
    "draw_after": 10_000,
    "games": 100_000,
    "method": play_a_first
}

random.seed(1337)

for game in range(scores["games"]):
    foo = [list(itertools.repeat(i, 4)) for i in range(1,14)]
    foo = list(itertools.chain(*foo))
    random.shuffle(foo)
    hand_A = foo[:len(foo)//2]
    hand_B = foo[len(foo)//2:]

    if game % 100 == 0:
        print(" "*10+"\r", end="")
        print(" " + str(round((game/scores["games"]) * 100, 2)) + "%\r", end="")

    moves = 0
    while True:
        res = scores["method"](hand_A, hand_B)
        moves += 1

        if res == END_A:
            scores["win_a"] += 1
            scores["avg_moves"] += moves
            break
        if res == END_B:
            scores["win_b"] += 1
            scores["avg_moves"] += moves
            break
        if res == END_OF_CARDS:
            scores["draw_no_cards"] += 1
            scores["avg_moves"] += moves
            break
        if moves > scores["draw_after"]:
            break

scores["no_draw"] = scores["win_b"] + scores["win_a"]
scores["draw_move_limit"] = scores["games"] - scores["no_draw"]
scores["avg_moves"] /= scores["no_draw"]
scores["no_draw_chance"] = scores["no_draw"] / scores["games"]
scores["win_a_chance"] = scores["win_a"]/scores["no_draw"]
scores["win_b_chance"] = scores["win_b"]/scores["no_draw"]

print(scores)
