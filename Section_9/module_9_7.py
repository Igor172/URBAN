def is_prime(func):
    def verify(*args):
        add = func(*args)
        count = 0
        for i in range(1, add + 1):
            if add % i == 0:
                count += 1
        return f'Простое \n{add}' if count == 2 else f'Составное \n{add}'
    return verify


@is_prime
def sum_three(*nums):
    return sum(nums)


result = sum_three(2, 3, 6)
print(result)
