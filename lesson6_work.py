#def recursion(n):
#    if n == 1:
#        return
#    return f"{recursion(n - 1)} {n}"
#print(recursion(1))


#def recursion(a,b):
#    if (a > b):
#        if(a ==b ):
#            return
#        return f"{a} {recursion(a -1, b)}"
#    else:
#        if(a ==b):
#            return a
#        return f"{a}{recursion(a+1, b)}"
#print(recursion(5,9))
#print(recursion(9,5))


#def recursion_3(n):
#    if n ==1:
#        return 1
#    elif n > 1 and n < 2:
#        return 0
#    else:
#        return recursion_3(n / 2)
#def main():
#    n = 3
#    if recursion_3(n) == 1:
#        print("yes")
#    else:
#        print("No")
#main()

#def recursion_4(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + recursion_4(n // 10)

#print(recursion_4(346))



#def recursion_5(n):
#    if n < 10:
#        return n
#    else:
#        print(f"{n % 10}", end="")
#        return recursion_5(n // 10)
#print(recursion_5(34))
