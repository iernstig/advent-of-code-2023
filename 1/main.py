import re
with open("input.txt", "r") as f:
    lines = [l.rstrip().strip() for l in f.readlines()]

calibration = 0
for line in lines:
    search_result = re.findall("\d", line)
    if search_result != []:
        calval = int(search_result[0] + search_result[-1])
        calibration += calval

print(calibration)
