import json


def diff(extended, abbreviated):
    dic_ext = {el[0]: el for el in extended}
    dic_abbr = {el[0]: el for el in abbreviated}
    dic_r = {}
    name = 4
    country = 5
    long = 1
    lat = 2
    ddate = 3
    set_boat_ext = {boat for boat in dic_ext}
    set_boat_abr = {boat for boat in dic_abbr}
    set_only_ext = set_boat_ext - set_boat_abr
    set_on_both = set_boat_ext & set_boat_abr
    set_id_only_abbr = set_boat_abr - set_boat_ext

    return ({dic_ext[boat_e][name] for boat_e in set_only_ext},
            {dic_ext[boat_a][name] for boat_a in set_on_both},
            set_id_only_abbr)



with open("marine-e2-ext.json", encoding="utf-8") as feed:
    extended_full = json.load(feed)

with open("marine-e2-abb.json", encoding="utf-8") as feed:
    abbreviated_full = json.load(feed)

print(diff(extended_full, abbreviated_full))