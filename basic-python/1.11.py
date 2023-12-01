str = input().lower()
del_sym = "!,.?;:#$%^&*(),"
i = len(del_sym) - 1
while i >= 0:
    str = str.replace(del_sym[i], "")
    i -= 1
str1 = str.split()
i = 0
res = []
while i < len(str1):
    if len(str1[i]) >= 5 and len(set(str1[i])) >= 4 and str1.count(str1[i]) > 2:
        res.append(str1[i])
    i += 1
res = set(res)
res_list = list(res)
res_list.sort()
i = 0
while i < len(res_list):
    print(res_list[i])
    i += 1
