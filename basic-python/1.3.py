interval_start = input()
interval_end = input()
flag = True
while num := input():
    if num >= interval_start and num <= interval_end:
        continue
    else:
        flag = False
print(flag)