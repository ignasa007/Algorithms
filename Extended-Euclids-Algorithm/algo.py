lst = list(map(int, input("Enter the two numbers - ").split()))

n1, n2 = lst
a1, a2 = 1, 0
b1, b2 = 0, 1
q = n1//n2
n1, n2 = n2, n1-q*n2

while n2!=0:
    a1, a2 = a2, a1-q*a2
    b1, b2 = b2, b1-q*b2
    q = n1//n2
    n1, n2 = n2, n1-q*n2
    
print("GCD = ", n1, " = ", a2, "*", lst[0], " + ", b2, "*", lst[1], sep="")
