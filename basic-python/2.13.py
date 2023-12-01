def del_sym(str):
    sym = "!@#%"
    i = len(sym) - 1
    while i >= 0:
        str = str.replace(sym[i], "")
        i -= 1
    return str
while str := input():
    if str[0] == "!":
        str = del_sym(str)
        print(str.upper())
    else:
        str = del_sym(str)
        print(str.lower())