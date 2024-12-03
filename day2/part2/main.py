def is_list_ordered(list1: list[int]) -> bool:
    """
    Checks if the list is sorted in ascending or descending order.
    """
    return list1 == sorted(list1) or list1 == sorted(list1, reverse=True)

def compare_list_elements(list1: list[int]) -> bool:
    """
    Checks that the absolute difference between consecutive elements 
    is at most 3, and that there are no duplicate elements.
    """
    for i in range(len(list1) - 1):
        if list1[i] == list1[i + 1] or abs(list1[i] - list1[i + 1]) > 3:
            return False
    return True

def is_safe(list1: list[int]) -> bool:
    """
    Determines if a list is "Safe" according to the rules.
    """
    return is_list_ordered(list1) and compare_list_elements(list1)

def can_be_made_safe(list1: list[int]) -> bool:
    """
    Checks if a list can be made "Safe" by removing one element.
    """
    for i in range(len(list1)):
        modified_list = list1[:i] + list1[i+1:]
        if is_safe(modified_list):
            return True
    return False

safe_count = 0

with open(r"F:\Desktop\Advent-Of-Calendar-2024\day2\part1\test.txt", "r") as file:
    data = file.readlines()

for datum in data:
    current_list = list(map(int, datum.strip().split()))
    if is_safe(current_list) or can_be_made_safe(current_list):
        safe_count += 1

print(f"Number of Safe reports: {safe_count}")