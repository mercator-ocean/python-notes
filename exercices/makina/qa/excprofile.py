import cProfile, pstats, io
pr = cProfile.Profile()

l1 = range(1, 2001)
l2 = range(1000, 3001)

def intersec_with_dict(l1, l2):
    result = []
    d = {}
    for i in l1:
        d[i] = None
    for i in l2:
        if i in d:
            result.append(i)
    return result


def intersec_with_list(l1, l2):
    result = []
    for i in l1:
        for j in l2:
            if j == i:
                result.append(j)
    return result


pr.enable() # début profiling

def test_intersec(*args):
    return intersec_with_dict(*args)  # changer la metode pour comparer

test_intersec(l1, l2)
pr.disable() # fin profiling



# statistiques
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
