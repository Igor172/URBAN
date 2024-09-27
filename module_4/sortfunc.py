nums_1 = [28, 1, 5, 3, 82, 16]
nums_2 = [5, 7, 47, 37, 27, 17, 89, 34]
nums_3 = [96, 1, 48, 3, 59, 67, 5, 13, 90, 1]

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
        ls[i], ls[lowest] = ls[lowest], ls[i]

def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls






bubble_sort(nums_1)
print(nums_1)
selection_sort(nums_2)
print(nums_2)
insertion_sort(nums_3)
print(nums_3)