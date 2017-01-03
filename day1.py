from time import time

def find_max(array):
    start_time = time()
    temp = array[0]
    for x in array:
        if x >= temp:
            temp = x
    end_time = time()
    print (end_time - start_time)
    return temp

