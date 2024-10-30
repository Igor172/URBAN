first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(el_1, el_2) for el_1 in first_strings for el_2 in second_strings if len(el_1) == len(el_2)]
third_result = {x : len(x) for x in (first_strings + second_strings) if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)