def power(x, n):
    # if not n:
    #     return 1
    # if n == 1:
    #     return x
    # if not n % 2:
    #     racine = power(x, n/2)
    #     return racine * racine
    # return x * power(x, n-1)

    puissance = bin(n)
    result = x
    index = 3
    while index < len(puissance):
        print(locals())
        result = result * result
        if puissance[index] == '1':
            result = result * x
        index += 1

    return result

print(power(2,5))