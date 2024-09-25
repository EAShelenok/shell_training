def test_function():
    b = 7
    def inner_function():
        print("Я в области видимости функции 'test_function'")
        b = 5
        return b
    return b + inner_function()

res_1 = test_function()
#res_2 = inner_function() #возникнет ошибка (область видимости) inner_function() ограничена областью действия
                          #test_function()
print(res_1)