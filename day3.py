# recursion

def factorial(n):
    # base case
    if n == 0:
        return 1
    #recursive call
    return n* factorial(n-1)


#english ruler

def draw_line(line_len, line_label = ""):
    line = "-"*line_len
    if line_label :
        line += line_label
    print line

def draw_interval(central_len):
    if central_len > 0 :
        draw_interval(central_len - 1)
        draw_line(central_len)
        draw_interval(central_len - 1)

def draw_ruler(ruler_inch, major_len):

    draw_line(major_len)
    for i in range(ruler_inch):
        draw_interval(ruler_inch-1)
        draw_line(major_len, str(i+1))

def search(array, n):
    for x in array:
        if x == n:
            return True
    return False

def binary_search(array, num, low, high):
    mid = ( low + high )/2

    if num == array[mid]:
        return True
    elif num > array[mid]:
        return binary_search(array, num , mid+1, high)
    elif num < array[mid]:
        return binary_search(array, num , low, mid-1)
    elif low > high :
        return False
#get size of dir

import os
# os.path.getsize(path) returns immidiate size
# os.path.join(a,b) joins path
# os.path.isdir(path) returns if a dir or not
# os.listdir(path) returns all dir



def get_size(path):
    if os.path.isdir(path):
        for filenames in os.lisdir(path):
            return os.path.getsize(path) + get_size(os.path.join(path,filenames))
    return os.path.getsize(path)



#reverse an array

def reverse(A, start, end):
    if start < end:
        A[start] A[end] = A[end],A[start]
        return reverse(A,start+1, end-1)


def max(array, n):
    if n<=1 :
        return array[0]
    elif array[0] > array[-1]:
        return max(array[:n-1],n-1)
    else:
        return max(array[1:n],n-1)


#algo to multiply numbers

def product(num1,num2):
    if num1/10 == 0 and num2/10 == 0:
        return num1*num2
    elif num1/10 != 0 :
        return product(num1%10,num2) + 10*product(num1/10,num2)
    elif num2/10 != 0 :
        return product(num1,num2%10) + 10*product(num1,num2/10)







