import re

def part1():
    with open("input.txt", "r") as f:
        games = [l.rstrip().split("|") for l in f.readlines()]
        s = 0
        for card, game in games:
            card_nums = [int(x.strip()) for x in re.findall("\d+ ", card)]
            game_nums = {int(x.strip()): True for x in re.findall("\d+", game)}
            matches = -1
            for card_num in card_nums:
                if card_num in game_nums:
                    matches+=1


            game_result =  2 ** matches
            if game_result > .5:
                s += game_result

        print(s)
            

def part2():
    with open("input.txt", "r") as f:
        games = [l.rstrip().split("|") for l in f.readlines()]
        card_dict = {i + 1: 1 for i in range(len(games))}
        for i, (card, game) in enumerate(games):
            card_nums = [int(x.strip()) for x in re.findall("\d+ ", card)]
            game_nums = {int(x.strip()): True for x in re.findall("\d+", game)}
            matches = 0
            for card_num in card_nums:
                if card_num in game_nums:
                    matches+=1

            for i_match in range(i+1, i+ matches+1):
                card_dict[i_match + 1] += card_dict[i + 1]


        
        print(sum(card_dict.values()))            

part2()



