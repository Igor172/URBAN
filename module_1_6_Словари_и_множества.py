my_dict = {'Alex' : 2000, 'Max' : 2002, 'Sophy' : 2004, 'Frieda' : 2003}
print(my_dict)
print(my_dict.get('Frieda', 'Имя отсутствует'))
print(my_dict.get('Anton', 'Имя отсутствует'))

my_dict['Ivan'] = 1999
my_dict.update({'Mary' : 2001, 'Sam' : 1998})
print(my_dict)
year = my_dict.pop('Ivan')
print(my_dict)
print(year)

my_set = {18, 3.5, True, 18, 'Ok', False, 'Ok'}
print(my_set)
my_set.add('1000')
my_set.add((3, 2, 1))
print(my_set)
my_set.discard(False)
print(my_set)