from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    l = []
    for key, _ in d.items():
        l.append(key)
    l_sort = sorted(l, reverse=True)
    return l_sort
    

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
