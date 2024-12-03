import re

with open(r"F:\Desktop\Advent-Of-Calendar-2024\day3\part1\text.txt", "r") as file:
    data = file.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, data)

total = sum(int(x) * int(y) for x,y in matches)

print(total)