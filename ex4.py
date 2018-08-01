def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i):
            j = i - j - 1
            if(list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
def bubble_sort(list):
    for i in range(len(list)):
        i = len(list) - 1 - i
        for j in range(i):
            if(list[j + 1] < list[j]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

some_list  = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
]

print(some_list)
#insertion_sort(some_list)
#bubble_sort(some_list)
#sorted(some_list)
#some_list.sort()
print(some_list)
