def prefixAverage(array):
    temp = [0]*len(array)
    temp[0] = array[0]
    for i in range(1, len(array)):
        temp[i] += (temp[i-1]+array[i])/(i+1)
    return temp

# big-oh(n^3) algo


def setDisjoint(A, B, C):
    for x in A:
        for y in B:
            for z in C:
                if x == y == z:
                    return False
    return True

# other algo BOG-OH(n^2)


def setDisjoint2(A, B, C):
    for x in A:
        for y in B:
            if x == y:
                if x in C:
                    return False
    return True
# poor algo


def eleUnique(array):
    for x in range(len(array)):
        for y in range(x+1, len(array)):
            if array[x] == array[y]:
                return False
    return True

# better algo


def unique(array):
    array.sort()
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            return False
    return True
