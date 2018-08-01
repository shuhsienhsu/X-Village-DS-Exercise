from lib.stack import Stack
from lib.queue import Queue

def finding_cheese(map, mouse):
    s = Stack()
    sx = Stack()
    sy = Stack()
    for i in range(10000):
        if(s.isEmpty() == False):
            j = s.pop()
        k = 1
        if((map[mouse[0]][mouse[1]+1] == 0 or map[mouse[0]][mouse[1]+1] == 5) and k == 1):
            if(map[mouse[0]][mouse[1]+1] == 5):
                sx.push(mouse[0])
                sy.push(mouse[1])
                cheese = [[mouse[0], mouse[1]+1]]
                while(sx.isEmpty() == False):
                    cheese += [[sx.pop(), sy.pop()]]
                return cheese
            sx.push(mouse[0])
            sy.push(mouse[1])
            map[mouse[0]][mouse[1]+1] = 2
            mouse[1] += 1
            s.push(0)
            k = 1
        elif((map[mouse[0]+1][mouse[1]] == 0 or map[mouse[0]+1][mouse[1]] == 5) and (k == 1 or j == 0)):
            if(map[mouse[0]+1][mouse[1]] == 5):
                sx.push(mouse[0])
                sy.push(mouse[1])
                cheese = [[mouse[0]+1, mouse[1]]]
                while(sx.isEmpty() == False):
                    cheese += [[sx.pop(), sy.pop()]]
                return cheese
            sx.push(mouse[0])
            sy.push(mouse[1])
            map[mouse[0]+1][mouse[1]] = 2
            mouse[0] += 1
            s.push(1)
            k = 1
        elif((map[mouse[0]][mouse[1]-1] == 0 or map[mouse[0]][mouse[1]-1] == 5) and (k == 1 or j == 1)):
            if(map[mouse[0]][mouse[1]-1] == 5):
                sx.push(mouse[0])
                sy.push(mouse[1])
                cheese = [[mouse[0], mouse[1]-1]]
                while(sx.isEmpty() == False):
                    cheese += [[sx.pop(), sy.pop()]]
                return cheese
            sx.push(mouse[0])
            sy.push(mouse[1])
            map[mouse[0]][mouse[1]-1] = 2
            mouse[1] -= 1
            s.push(2)
            k = 1
        elif((map[mouse[0]-1][mouse[1]] == 0 or map[mouse[0]-1][mouse[1]] == 5) and (k == 1 or j == 2)):
            if(map[mouse[0]-1][mouse[1]] == 5):
                sx.push(mouse[0])
                sy.push(mouse[1])
                cheese = [[mouse[0]-1, mouse[1]]]
                while(sx.isEmpty() == False):
                    cheese += [[sx.pop(), sy.pop()]]
                return cheese
            sx.push(mouse[0])
            sy.push(mouse[1])
            map[mouse[0]-1][mouse[1]] = 2
            mouse[0] -= 1
            s.push(3)
            k = 1
        else:
            k = 0
            mouse[0] = sx.pop()
            mouse[1] = sy.pop()

map = [[1,1,1,1,1,1,1,1],[1,0,0,0,1,1,1,1],[1,0,0,0,0,1,1,1],
        [1,0,1,1,1,1,1,1],[1,0,1,1,1,1,1,1],[1,0,0,0,1,1,1,1],
        [1,5,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
mouse = [1, 1]
cheese = finding_cheese(map, mouse)
for i in range(len(cheese)):
    i = len(cheese) - 1 - i
    print(cheese[i])