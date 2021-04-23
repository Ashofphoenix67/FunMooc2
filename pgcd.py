def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(pgcd(15,10))
