import re

with open("./input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

keys = [
"seed-to-soil map:",
"soil-to-fertilizer map:",
"fertilizer-to-water map:",
"water-to-light map:",
"light-to-temperature map:",
"temperature-to-humidity map:",
"humidity-to-location map:"
]

seeds = [int(x) for x in lines[0].split("seeds: ")[-1].split(" ")]

data = {k: [] for k in keys}
current_key = None
for line in lines[1:]:
    for key in keys:
        if key in line:
            current_key = key
    if current_key and re.match("\d", line):
        items = [int(x) for x in line.split(" ")]
        destination = items[0]
        source = items[1]
        length = items[2]
        data[current_key].append([source, destination, length])



locations = []
for seed in seeds:
    for key in keys:
        print(key)
        for source, destination, length in data[key]:
            if source <= seed <= source + length:
                seed = destination + abs(source - seed)
                break
    locations.append(seed)

print(min(locations))