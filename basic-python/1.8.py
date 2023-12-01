num = int(input())
maxs = []
while num >= 1:
    list_num = input()
    maxs.append(int(max(list_num)))
    num -= 1
maxs.sort(reverse=True)
maxs_str = ";".join(map(str, maxs))
print(maxs_str, sep=';')