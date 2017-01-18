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

a = input("Wanna try more?(Y/N)")
while(a == 'Y'):
    num1 = int(input("Input num1"))
    num2 = int(input("Number2"))
    print product(num1,num2)
    a = input("Wanna try more")

