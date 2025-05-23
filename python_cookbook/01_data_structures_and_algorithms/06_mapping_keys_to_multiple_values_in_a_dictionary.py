from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
print(d)

#######################################################################

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
d['b'].add(4)
d['b'].add(5)
print(d)

#######################################################################

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)