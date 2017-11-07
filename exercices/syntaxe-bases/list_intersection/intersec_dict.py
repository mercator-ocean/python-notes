l1 = range(1, 2001)
l2 = range(1000, 3001)


def intersec(l1, l2):
    result = []
    d = {}
    for i in l1:
        d[i] = None
    for i in l2:
        if i in d:
            result.append(i)
    return result


for _ in range(10):
    result = intersec(l1, l2)
