l1 = range(1, 2001)
l2 = range(1000, 3001)


def intersec(l1, l2):
    result = []
    for i in l1:
        for j in l2:
            if j == i:
                result.append(j)
                break
    return result


for _ in range(10):
    result = intersec(l1, l2)
