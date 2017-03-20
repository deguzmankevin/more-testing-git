def merge(s0,s1):
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None)
    while True:
        if e0 == None and e1 == None:
            raise StopIteration
        elif e1 == None:
            yield e0
            e0 = next(i0, None)
        elif e0 == None:
            yield e1
            e1 = next(i1, None)
        elif e0 < e1:
            yield e0
            e0 = next(i0, None)
        elif e1 < e0:
            yield e1
            e1 = next(i1, None)
        
        elif e0 == e1:
            yield e0
            e0 = next(i0, None)
            e1 = next(i1, None)
m = merge([1, 2, 3, 6, 8], [4, 5, 6])