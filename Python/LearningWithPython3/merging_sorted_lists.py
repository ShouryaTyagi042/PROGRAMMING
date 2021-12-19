def merge(xs , yz) :
    xi = 0
    yi = 0
    xs_len = len(xs)
    yz_len = len(yz)
    result = []
    while True :
        if xi >= xs_len :
            result.extend(yz[yi:])
            break
        elif yi >= yz_len :
            result.extend(xs[xi:])
            break
        elif xs[xi] <= yz[yi] :
            result.append(xs[xi])
            xi += 1
        else :
            result.append(yz[yi])
            yi += 1
    return result
def present_in_both(xs,yz) :
    xi = 0
    yi = 0
    xs_len = len(xs)
    yz_len = len(yz)
    result = []
    while True :
        if xi >= xs_len :
            # result.extend(yz[yi:])
            break
        elif yi >= yz_len :
            # result.extend(xs[xi:])
            break
        elif xs[xi] < yz[yi] :
            # result.append(xs[xi])
            xi += 1
        elif xs[xi] == yz[yi] :
            result.append(xs[xi])
            xi += 1
        else :
            # result.append(yz[yi])
            yi += 1
    return result
def unique_to_first(xs,yz) :
    xi = 0
    yi = 0
    xs_len = len(xs)
    yz_len = len(yz)
    result = []
    while True :
        if xi >= xs_len :
            # result.extend(yz[yi:])
            break
        elif yi >= yz_len :
            result.extend(xs[xi:])
            break
        elif xs[xi] < yz[yi] :
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == yz[yi] :
            # result.append(xs[xi])
            xi += 1
        else :
            # result.append(yz[yi])
            yi += 1
    return result
def unique_to_second(xs,yz) :
    xi = 0
    yi = 0
    xs_len = len(xs)
    yz_len = len(yz)
    result = []
    while True :
        if xi >= xs_len :
            result.extend(yz[yi:])
            break
        elif yi >= yz_len :
            # result.extend(xs[xi:])
            break
        elif xs[xi] > yz[yi] :
            result.append(yz[yi])
            yi += 1
        elif xs[xi] == yz[yi] :
            # result.append(xs[xi])
            yi += 1
        else :
            # result.append(yz[yi])
            xi += 1
    return result
def bagdiff(xs,yz) :
    xi = 0
    yi = 0
    xs_len = len(xs)
    yz_len = len(yz)
    result = []
    while True :
        if xi >= xs_len :
            # result.extend(yz[yi:])
            break
        elif yi >= yz_len :
            # result.extend(xs[xi:])
            break
        elif xs[xi] < yz[yi] :
            # result.append(xs[xi])
            xi += 1
        elif xs[xi] == yz[yi] :
            xs.pop(xi)
            xi += 1
            yi += 1
        else :
            # result.append(yz[yi])
            yi += 1
    return xs



l1 = [1,3,5,7]
l2 = [2,4,6,8,10,12]
l3 = [2,4,8,16]

print(merge(l1,l2))
print(present_in_both(l2,l3))
print(unique_to_first(l2,l3))
print(unique_to_second(l2,l3))
print(bagdiff([5,7,11,11,11,12,13], [7,8,11]))
