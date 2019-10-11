def function():
    var = 'local env'
    print(var)

var = 'global env'
function()
print(var)