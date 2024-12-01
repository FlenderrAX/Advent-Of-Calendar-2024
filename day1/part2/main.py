import random

FIRST_LIST: list[int] = [random.randint(0, 20) for _ in range(10)]
SECOND_LIST: list[int] = [random.randint(0, 20) for _ in range(10)]

calculate_list_dist = lambda list1, list2: sum(list2.count(i) * i for i in list1)

print(calculate_list_dist(FIRST_LIST, SECOND_LIST))