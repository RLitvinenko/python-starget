namedefault = 'Roman'
bname = (str(input('Введите свое имя')))
def hello(bnametest):
    if bname or namedefault:
        return namedefault
#    else:
#        return bname
print(bnametest)


#def hello(name):
#    if not name:
#        return
#    print('hello,', name, '!', sep='')
#hello('Alex')
#hello('')
#hello('python')