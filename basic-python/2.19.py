def repeat_deco(n=1):
    def decorator(func):
        def repeat(*args, **kwargs):
            res = None
            for _ in range(n):
                res = func(*args, **kwargs)
            return res
        return repeat
    return decorator

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)