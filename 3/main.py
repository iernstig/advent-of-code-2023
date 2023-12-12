import re

with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

symbol_map = {} # (i_line, symbol_index) -> e.g. coordinate
number_list = [] # number -> (i_line, span)
for i_line, line in enumerate(lines):

    symbol_matches = [m for m in re.finditer("\D", line) if m.group(0) != "."]
    for symbol_match in symbol_matches: 
        symbol_index = symbol_match.span()[0]
        symbol_map[(i_line, symbol_index)] = True

    number_matches = re.finditer("\d+", line)
    print(line)
    for number_match in number_matches:
        number_list.append((int(number_match.group(0)), (i_line, number_match.span())))




def is_valid(i_line, span):
    span_length = span[1] - span[0]
    coords_which_could_contain_symbol = [*list(zip([i_line - 1]*(span_length+3), range(span[0] - 1, span[1] + 1))), 
                                         *list(zip([i_line + 1]*(span_length+3), range(span[0] - 1, span[1] + 1))), (i_line, span[0] - 1), (i_line, span[1])]

    for coord in coords_which_could_contain_symbol:
        if coord in symbol_map:    
            return True

    return False

s = 0
for num, (i_line, span) in number_list:
    if is_valid(i_line, span):
        s += num

print(s)
    

