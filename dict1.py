def graph_dict(filename):
    with open(filename, encoding='utf-8') as f:
        lig = f.readline()
        dic={}
        while lig != '':
            el = lig.split()
            val = (el[2], int(el[1]))
            if el[0] not in dic:
                dic.setdefault(el[0], [val])
            else:
                dic[el[0]].append(val)
            lig = f.readline()
    return dic



graph_dict('graph1.txt')