def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i):
            j = i - j - 1
            if(list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            else:
                break
def bubble_sort(list):
    for i in range(len(list)):
        i = len(list) - 1 - i
        for j in range(i):
            if(list[j + 1] < list[j]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
#def merge_sort(list):
#def quick_sort(list):
        

mylist = [4,3,2,1]
print(mylist)
insertion_sort(mylist)
print(mylist)
mylist2 = [2,4,3,1]
print(mylist2)
bubble_sort(mylist2)
print(mylist2)