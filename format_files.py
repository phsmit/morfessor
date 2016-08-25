#!/usr/bin/env python3

out_dict = open('dict', 'w', encoding='utf-8')
out_model = open('model2.txt', 'w', encoding='utf-8')

for line in open('model.txt', encoding='utf-8'):
    if line.startswith('#'):
        print(line.strip(), file=out_model)
        continue

    count, rest = line.split(None, 1)
    parts = rest.strip().split(" + ")
    nparts = []
    
    for i, p in enumerate(parts):
        key, trans = p.rsplit('/', 1)
        if len(trans) < 1:
            trans = "SPN"
        nparts.append(key)
        if i != 0:
            key = "+" + key
        if i != len(parts) -1:
            key = key + "+"
        print("{}\t{}".format(key, trans.replace(",", " ")), file=out_dict)
    print("{} {}".format(count, " + ".join(nparts)), file=out_model)
