from lib.stack import Stack
from lib.queue import Queue

def base_converter(dec, base):
    digits = "0123456789ABCDEF"
    i = 0
    for j in range(10000):
        if(dec // (base**j) == 0):
            i = j
            break
    q = Queue()
    for k in range(i):
        k = i - k
        temp = dec % (base ** k) // (base ** (k-1))
        q.enqueue(digits[temp])
    str_temp = ""
    for l in range(i):
        str_temp += str(q.dequeue())
    return str_temp

print(base_converter(42, 2))
print(base_converter(1000, 16))
print(base_converter(700, 12))