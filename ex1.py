from lib.stack import Stack

def dec_to_bin(dec):
    i = 0
    for j in range(10000):
        if(dec // (2**j) == 0):
            i = j - 1
            break
    binary = 0
    for k in range(i):
        k = i - k
        if(dec % (2**(k + 1)) // (2**k) == 1):
            binary += 10 ** k
    return binary

def dec_to_bin2(dec):
    s = Stack()
    i = 0
    for j in range(10000):
        if(dec // (2**j) == 0):
            i = j
            break
    binary = 0
    for k in range(i):
        k = i - k
        if(dec % (2 ** k) // (2 ** (k-1)) == 1):
            s.push(1)
        else:
            s.push(0)
    for l in range(s.size()):
        binary += s.pop() * (10 ** l)
    return binary

print(dec_to_bin(42))
print(dec_to_bin(100))

print(dec_to_bin2(42))
print(dec_to_bin2(100))