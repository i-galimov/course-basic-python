num1 = int(input())
num2 = round(float(input()), 2)
num3 = int(input())
print(f'{num1:0=+10}')
print(f'{num2:#>10.2f}')
str3 = (f'{num3:0=16b}')
res = str3[0:4] + '_' + str3[3:7] + '_' + str3[6:10] + '_' + str3[9:13]
print(res)