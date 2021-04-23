def read_set(filename):
    with open(filename, encoding="utf-8") as f:
        lig = f.readline()
        lst = []
        sref = set()
        while lig != '':
            lst.append(lig.strip())
            lig = f.readline()
        sref.update(lst)
    return lst

def search_in_set(file_ref,filen):
    ref = read_set(file_ref)
    ret = []
    checklist = []

    with open(filen, encoding="utf-8") as f:
        lig = f.readline()
        while lig != '':
            checklist.append(lig.strip())
            lig = f.readline()

    for ckc in checklist:
        ret.append((ckc, ckc in ref))

    return ret



print(search_in_set('setref1.txt','setsample1.txt'))