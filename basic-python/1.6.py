str = input()
str = str.lower()
list = list(str)
#"!”, “%”, “#”, “@”
count = 0
for i in str:
    if i == "!" or i == "%" or i == "#" or i == "@":
        count += 1
print(count)
str2 = str.replace("!", "")
str3 = str2.replace("%", "")
str4 = str3.replace("#", "")
str5 = str4.replace("@", "")
print(str5)