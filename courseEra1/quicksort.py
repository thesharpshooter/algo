import os
def quickSort(array):
    n = len(array)
    if n <=1 :
        print array
        return array
    pivot = array[-1]
    i = 0
    j = 1
    while j < n-1 :
        if array[j] < pivot:
            i += 1
            array[i],array[j]=array[j],array[i]
        j += 1
    array[-1],array[i] = array[i],array[-1]
    return quickSort(array[:i+1])+[pivot]+quickSort(array[i+1:-1])

with open("assign2.txt","r") as data:
    array = []
    for line in data :
        array.append(line)
array = map(int,array)
print array
print quickSort(array)
