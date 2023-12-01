word = input()
words = word.split()
count = []
for i in words:
    count.append(len(i))
average = (max(count) + min(count)) / 2
print(average)