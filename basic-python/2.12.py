def average(*nums):
    sum = 0
    for i in nums:
        sum += i
    count = len(nums)
    res = sum / count
    print(res)
while num := input().split():
    result = list(map(int, num))
    average(*result)