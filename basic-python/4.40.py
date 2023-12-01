from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    deq = deque(nums)
    deq.rotate(n)
    return list(deq)
    

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)