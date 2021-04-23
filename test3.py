def test(a, b):
    try:
        return (a/b)
    except ZeroDivisionError:
        return "impossible"

print(test(5, 0))