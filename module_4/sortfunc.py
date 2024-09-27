nums_1 = [28, 1, 5, 3, 82, 16]
nums_2 = [5, 7, 47, 37, 27, 17]

def bubble_sort(ls):
    '''Сортировка пузырьком'''
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True

def selection_sort(ls):
    '''Сортировка выборкой'''
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[j], ls[lowest] = ls[lowest], ls[j]

bubble_sort(nums_2)
print(nums_2)
selection_sort(nums_2)
print(nums_2)

