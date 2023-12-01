from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    diff = 0
    if len(values_list_1) != len(values_list_2):
        diff = abs(len(values_list_1) - len(values_list_2))
    if len(values_list_1) > len(values_list_2):
        while diff > 0:
            values_list_2.append(1)
            diff -= 1
    elif len(values_list_1) < len(values_list_2):
        while diff > 0:
            values_list_1.append(1)
            diff -= 1

    result = []
    for i in range(len(values_list_1)):
        result.append(tuple((values_list_1[i], values_list_2[i])))
    return result




code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)