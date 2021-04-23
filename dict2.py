import json

def merge(extended, abbreviated):
    dic_ext = {el[0]: el for el in extended}
    dic_abbr = {el[0]: el for el in abbreviated}
    dic_r = {}
    name = 4
    country = 5
    long = 1
    lat = 2
    ddate = 3

    for boat in dic_ext:
        dic_r.setdefault(boat, [dic_ext[boat][name], dic_ext[boat][country],
                         (dic_ext[boat][long], dic_ext[boat][lat], dic_ext[boat][ddate]),
                         (dic_abbr[boat][long], dic_abbr[boat][lat], dic_abbr[boat][ddate])])

    return dic_r

with open("marine-e1-ext.json", encoding="utf-8") as feed:
    extended_full = json.load(feed)

with open("marine-e1-abb.json", encoding="utf-8") as feed:
    abbreviated_full = json.load(feed)

merge(extended_full, abbreviated_full)