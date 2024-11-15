def som(*args, neg: bool = False) -> int:
    s = 0
    for i in args:
        if neg:
            if i < 0:
                i = 0
            s += i
        else:
            s += i           
    return s


print(som(1, -2, 4, 5, neg=False))  