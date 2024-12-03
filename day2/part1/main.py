def is_list_ordered(lst: list[int]) -> bool:
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def compare_list_elements(lst: list[int]) -> bool:
    return all(abs(lst[i] - lst[i + 1]) <= 3 and lst[i] != lst[i + 1] for i in range(len(lst) - 1))

def is_safe(lst: list[int]):
    return compare_list_elements(lst) and is_list_ordered(lst)

first_list = []
safe_count = 0

with open(r"file.txt", "r") as file:
    data = file.readlines()
    for datum in data:
        first_list.append(list(map(int, datum.strip().split())))

for _ in first_list:
    safe_count += 1 if is_safe(_) else safe_count