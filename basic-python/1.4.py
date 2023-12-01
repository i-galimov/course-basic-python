str = input()
flag = True
flag2 = False
for i in str:
    if i == 'i' or i == 'e':
        flag = False
        break
    elif i == 'o' or i == 'a':
        flag2 = True
if flag and flag2:
    print(flag)
else:
    print(False)