import json
from collections import defaultdict
from pprint import pprint

with open('districts_mo.json', 'r') as mo:
    mo = json.load(mo)

with open('m_districts_id_map.json', 'r') as mo_id:
    mo_id = json.load(mo_id)


# for key, val in mo_id.items():
#     print(key, val)


d = defaultdict(dict)
p = defaultdict(dict)
prev_key = True
for key, val in mo.items():
    for i in val:
        if key != prev_key:
            print(p)
            d[key] = p
            d[key]['checked'] = True
        for k, v in mo_id.items():

            if i == v:
                # print(key, k, i, v)
                p[k] = {'text': i, 'checked': True}
    prev_key = key
    p = defaultdict(dict)

                # d[key] = {k: {'text': i, 'checked': True} for i in val}
    # print(key, val)

# d = {'key': {'val1': '', 'val2': ''}}
pprint(d)
json_obj = json.dumps(d, ensure_ascii=False)
with open('new_json.json', 'w', encoding='utf8') as nj:
    nj.write(json_obj)
# pprint(p)

