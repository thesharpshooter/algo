def find_max(array):
    temp = array[0]
    for x in array:
        if x >= temp:
            temp = x
    return temp

