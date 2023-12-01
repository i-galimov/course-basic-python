start, end, step = input().split()
for i in map(lambda x: x ** 2 if x % 2 == 1 else x * -1, range(int(start), int(end), int(step))):
   print(i)