# constraint: 12 red, 13 green, 14 blue
import re
with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]


def set_possible(rgb: tuple):
    return rgb[0] <= 12 and rgb[1] <= 13 and rgb[-1] <= 14

def game_possible(rgbs):
    return all([set_possible(rgb) for rgb in rgbs])

possible_index_count = 0
for line in lines: # each line is a game with several sets
    game = line.split(":")
    gamekey = game[0]
    gameindex = int(gamekey.split(" ")[-1])
    gamestrings = game[-1].split(";")

    rgbs = []
    for game_set in gamestrings:

        rgb = [0,0,0]
        for color_string in game_set.split(","):
            amount = int(re.findall("\d+", color_string)[0])
            color = [x.strip() for x in re.findall("\D+",color_string) if x != " "][0]
            if color == "red":
                rgb[0] = amount
            if color == "green":
                rgb[1] = amount
            if color == "blue":
                rgb[-1] = amount
        rgbs.append(rgb)

    if game_possible(rgbs):
        possible_index_count += gameindex

print(possible_index_count)

        



