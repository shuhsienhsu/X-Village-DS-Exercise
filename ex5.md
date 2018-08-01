1.
some_list.sort()是直接對原本的序列進行排序。
sorted(some_list)則是回傳一個排序過後的序列，不更動原本傳入的序列。

2.
Python使用的是Timsort，從merge sort和insertion sort演變而來。
它能夠先找到已經排序好的序列片段，使排序的效率提升。