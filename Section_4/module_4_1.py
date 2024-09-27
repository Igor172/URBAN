from fake_math import divide as fake_div
from true_math import divide as true_div

result1 = fake_div(15, 7)
result2 = fake_div(999, 0)
result3 = true_div(225, 15)
result4 = true_div(824, 0)

print(result1)
print(result2)
print(result3)
print(result4)