import numpy as np
with open("input.txt", "r") as f:
    lines = f.readlines()

x = {k: v for k, v in [line.rstrip().split("=") for line in lines]}
d = {}
for k, v in x.items():
    d[k.strip()] = (v.split(",")[0].strip().replace("(", ""), v.split(",")[1].strip().replace(")", ""))

with open("path.txt", 'r') as f:
    path = list(f.read().rstrip())

start = "AAA"
def recursive_shortest_path(node, already_visited=[]) -> int:
    already_visited.append(node)
    if node == "ZZZ":
        return 0
    if d[node][0] in already_visited and d[node][1] in already_visited:
        return np.inf
    if d[node][0] in already_visited:
        return 1 + recursive_shortest_path(d[node][1], already_visited)
    if d[node][1] in already_visited:
        return 1 + recursive_shortest_path(d[node][0], already_visited)

    return min(1 + recursive_shortest_path(d[node][0], already_visited), 1 + recursive_shortest_path(d[node][1], already_visited))
    
# print(recursive_shortest_path(start))    
def traverse():
    node = "AAA"
    stepcount = 0
    while 1:
        for step in path:
            if step == "L":
                node = d[node][0]
            else:
                node = d[node][1]
            stepcount+=1
            print(node)
            if node == "ZZZ":
                return stepcount


def find_start_nodes():
    start_nodes = []
    for k in d.keys():
        if k[-1] == "A":
            start_nodes.append(k)
    return start_nodes


def part2():
    node_keys = find_start_nodes()
    step_count = 0
    while 1:
        for step in path:
            direction = 0 if step == "L" else 1     
            node_keys = [d[node_key][direction] for node_key in node_keys]
            step_count += 1
            print([node_key[-1] == "Z" for node_key in node_keys])
                # return step_count
        
print(part2())


