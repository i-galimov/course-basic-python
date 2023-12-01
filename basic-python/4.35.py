
from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    result = defaultdict(list)
    for specialization in specializations:
        result[specialization[0]].append(specialization[1])
    return dict(result)


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)