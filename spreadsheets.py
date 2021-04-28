def spreadsheet(index):
    if index <= 0:
        return ""
    elif index <= 26:
        return chr(64 + index)
    else:
        return spreadsheet(int((index - 1) / 26)) + chr(65 + (index - 1) % 26)

print(spreadsheet(703))
