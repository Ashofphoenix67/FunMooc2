def fctf(input):
    if not input:
        return False
    else:
        return True

def fctg(input):
    return False

def compare_args(fctf, fctg, entree):
    res = []
    for el in entree:
        print(el)
        print(*el)
        res.append(fctf(*el) == fctg(*el))
    return res




print(compare_args(fctf, fctg, [(0,), (1,), (5,)]))