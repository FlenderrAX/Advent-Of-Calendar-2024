import re

with open(r"text.txt", "r") as file:
    data = file.read()

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, data)

for i in range(len(matches) - 1, -1, -1):
    if matches[i] == "don't()":
        matches.pop(i)
        if i + 1 < len(matches):
            matches.pop(i)

filtered_matches = [cmd for cmd in matches if cmd != 'do()']

total = 0
for cmd in filtered_matches:
    if cmd.startswith("mul"):
        x, y = map(int, re.findall(r"\d+", cmd))
        total += x * y

print(f"Matches : {matches}\nFiltered Matches : {filtered_matches}\nTotal : {total}")