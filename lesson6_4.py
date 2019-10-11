def outer_function():
    def inner_fuinctio():
        print("Внутреняя функция")
    print('Внешняя функция')
    inner_fuinctio()
outer_function()

#inner_function()