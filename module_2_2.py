first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)