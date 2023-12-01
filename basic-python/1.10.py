str = input().lower().split()
res = {x:str.count(x) for x in str}
word = max(res, key=res.get)
print(max(res, key=res.get), res[word])
