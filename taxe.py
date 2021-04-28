
def taxes(income):
    impot = 0
    if income > 150000:
        impot += 45 / 100 * (income-150000)
        income = 150000

    if 50001 <= income <= 150000:
        impot += 40 / 100 * (income-50000)
        income = 50000

    if 12501 <= income <= 50000:
        impot += 20 / 100 * (income-12500)

    return int(impot)

print(taxes(150000))