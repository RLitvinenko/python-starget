int_list= [1, 2, 3, 5]
char_list= ['a', 'c', 'z', 'x']
empty_list=[]

print("список чисел", int_list)
print("список символов", char_list)
print('пустой список', empty_list)
##
b = list('blablabla')
print(b)


##
def f(a, *args):
    print(a)
    print(args)

f('afjasf', 'afagas', 'agasgas')
