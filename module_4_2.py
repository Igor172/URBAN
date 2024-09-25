def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

print('Проведем тест')
test_function()

'''за счет вызова функции inner_function в теле функции test_function в консоль 
выводится текс "Я в области видимости функции test_function"'''

print('Проведем еще один тест')
inner_function()

'''при вызове функции inner_function() из глобальной области интерпритатор выдает 
ошибку, что функция не определена в этой области видимости'''