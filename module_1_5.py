immutable_var = (15, 8.5, 'Hello', True, [3, False, 'World'])
print(immutable_var)

immutable_var[2] = 'Hi' # Tuple не предоставляет возможность изменять объекты
print(immutable_var)
immutable_var[4][1] = True
print(immutable_var) #Если элемент кортежа - изменяемый объект, то его можно изменить, не изменяя всей остальной структуры

mutable_var = [True, 'Apple', 17, [4, 8, 12]]
print(mutable_var)
mutable_var[0] = 'It`s OK'  #Список предоставляет возможность изменять объекты списка
print(mutable_var)