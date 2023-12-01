from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    for i, k in zip(nums1, nums2):
        if i < k:
            res.append(nums1.index(i))
    return res
        

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)