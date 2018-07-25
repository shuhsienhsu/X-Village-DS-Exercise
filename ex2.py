from lib.queue import Queue

def hot_potato(name_list, num):
    q = Queue()
    for i in range(len(name_list)):
        q.enqueue(name_list[i])
    for i in range(len(name_list) - 1):
        for j in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    
    remaining_person = q.dequeue()

    return remaining_person

print(hot_potato(["Susan","Brad","Kent","David"], 6))
print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7))