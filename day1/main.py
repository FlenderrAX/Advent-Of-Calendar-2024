import random

def calculate_list_dist(list1: list[int], list2: list[int]) -> int:
    if (len(list1) != len(list2)):
        raise ValueError("Arrays must have the same size!")
    
    return sum(abs(nb1 - nb2) for nb1, nb2 in zip(sorted(list1), sorted(list2)))

FIRST_LIST: list[int] = [random.randint(0, 20) for _ in range(10)]
SECOND_LIST: list[int] = [random.randint(0, 20) for _ in range(10)]

print(calculate_list_dist(FIRST_LIST, SECOND_LIST))