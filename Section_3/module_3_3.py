def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(4, 5)
#print_params(3, 7, 8, 15) #Функция выдает ошибку, т.к. в нее передано 4 параметра вместо 3
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 'Word', 5]
values_dict = {'a' : 5, 'b' : False, 'c' : 'Urban'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 'String']
print_params(*values_list_2, 42)