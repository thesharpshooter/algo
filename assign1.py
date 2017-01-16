def merge(A, B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] <= B[0]:
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])


def mergeSort(array):
    n = len(array)
    if n == 1:
        return array
    A = mergeSort(array[:n//2])
    B = mergeSort(array[n//2:])
    return merge(A, B)

array = mergeSort([1, 321, 3214, 345., 4366654, 64, 543, 34])


myData = []
with open('courseEra1/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt') as myFile:
    for line in myFile:
        myData.append(int(line))
        # print line
# print myData


def mergeAndCount(A, B):
    temp = []
    i, j = 0, 0
    count = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(B[j])
            j += 1
            count += len(A)-i
    temp = temp + A[i:] + B[j:]
    return (temp, count)


def countInver(array):
    n = len(array)
    if n <= 1:
        return (array, 0)
    (A, a) = countInver(array[:n//2])
    (B, b) = countInver(array[n//2:])
    (C, c) = mergeAndCount(A, B)
    return (C, a+b+c)

result = countInver(myData)
print result[1]
