import math

# Multiply two number


def product(a, b):
    n1 = len(str(a))
    n2 = len(str(b))
    if n1 == 1 and n2 == 1:
        return a*b
    al = a//pow(10, (n1//2))
    ar = a % pow(10, (n1//2))
    bl = b//pow(10, (n2//2))
    br = b % pow(10, (n2//2))

    p1 = product(al, bl)
    p2 = product(ar, br)
    p3 = product((al+ar), (bl+br))

    return p1*pow(10, n1)+(p3-p1-p2)*pow(10, n1//2)+p2


# closest pair

# RETURNS DISTANCE BETWEEN TWO POINTS


def dis(A, B):
    return math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)


def closestPair(P):
    n = len(P)
    # IF LESS NO OF POINTS SIMPLY RETURN THEIR DISTANCE
    if n <= 3:
        d = 100000*100
        for i in range(n):
            for j in range(i+1, n):
                if dis(P[i], P[j]) < d:
                    d = dis(P[i], P[j])
        return d

    # SORT THE POINTS ACCORDING TO THEIR X COORDINATE
    Px = sorted(P)
    mid = Px[n//2]
    L = Px[:n//2]
    R = Px[n//2:]

    # MINIMUM OF THE TWO MINIMUM DISTANCE IS TAKEN
    dl = closestPair(L)
    dr = closestPair(R)
    d = min(dl, dr)

    # STRIP TAKE POINTS THAT ARE WITHIN THE RANGE OF 2DELTA(d)
    strip = []
    for p in P:
        if abs(p[0]-mid[0]) <= d and abs(p[1]-mid[1]) <= d and p != mid:
            strip.append(p)

    ns = len(strip)
    for j in range(ns):
        for k in range(j+1, ns):
            if dis(strip[j], strip[k]) < d:
                d = dis(strip[j], strip[k])
    return d

array = [[3, -1], [2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
print closestPair(array)
