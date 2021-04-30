def numbers(*args):
    try:
        return sum(args), min(args), max(args)
    except ValueError:
        return 0,0,0
print(numbers())