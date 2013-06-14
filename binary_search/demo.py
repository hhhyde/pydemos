def binarysearch(array, f, t, value):
    low = f
    high = t
    while low < high:
        mid = (low + high) >> 1
        print('-------%s--------' % mid)
        if mid < value:
            low = mid
        elif mid > value:
            high = mid
        else:
            return mid

binarysearch(range(100), 0, 99, 66)
