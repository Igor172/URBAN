grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(list(students), key=str.casefold)
print(students)

for el in range(len(grades)):
    grades[el] = sum(grades[el]) / len(grades[el])

print(grades)

final_dict = dict(zip(students, grades))
print(final_dict)