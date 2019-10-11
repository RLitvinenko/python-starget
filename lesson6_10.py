a = print

a("fjajgjag")
def my_sum(x):
    def my_sum1(y):
        return x + y
    return(my_sum1)
print(my_sum(5)(6))