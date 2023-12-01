import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = [date.split('-')[1] for date in dates]
    month_counter = Counter(months)
    top_n = month_counter.most_common(n)
    list = []
    for i in range(len(top_n)):
        list.append(top_n[i][0])
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)