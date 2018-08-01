class MinHeap:
    def build_heap(self, list):
        self.minheap = [0] + list
        self.to_sort()
        self.display()
    def insert(self, k):
        self.minheap += [k]
        self.to_sort()
        self.display()
    def del_min(self):
        self.min = self.minheap[1]
        self.minheap[1] = self.minheap[len(self.minheap) - 1]
        del self.minheap[len(self.minheap) - 1]
        self.to_sort()
        self.display()
        return self.min
    def display(self):
        for i in range(1, len(self.minheap)):
            print(self.minheap[i], end=' ')
        print()
    def to_sort(self):
        k = (len(self.minheap) - 1) // 2
        back_or_not = False
        for i in range(k):
            i = k - i
            if(i == 1):
                back_or_not = True
            result = self.to_sorting(i, back_or_not)
            while(result != 0):
                if(result <= (len(self.minheap) - 1) // 2):
                    result = self.to_sorting(result, back_or_not)
                else:
                    result = 0
    def to_sorting(self, i, back_or_not):
        try:
            if(self.minheap[i] > self.minheap[i * 2] or self.minheap[i] > self.minheap[i * 2 + 1]):
                temp = self.minheap[i]
                if(self.minheap[i * 2] < self.minheap[i * 2 + 1]):
                    self.minheap[i] = self.minheap[i * 2]
                    self.minheap[i * 2] = temp
                    if(back_or_not):
                        return i * 2
                elif(self.minheap[i * 2] > self.minheap[i * 2 + 1]):
                    self.minheap[i] = self.minheap[i * 2 + 1]
                    self.minheap[i * 2 + 1] = temp
                    if(back_or_not):
                        return i * 2 + 1
            return 0
        except Exception:
            if(self.minheap[i] > self.minheap[i * 2]):
                temp = self.minheap[i]
                self.minheap[i] = self.minheap[i * 2]
                self.minheap[i * 2] = temp
                if(back_or_not):
                    return i * 2
            return 0

    #not_this_one
    def to_sort02(self):
        k = len(self.minheap) - 1
        for i in range(len(self.minheap)):
            k = k // 2
            if(k == 0):
                k = i
                break
        for j in range(k):
            for i in range(len(self.minheap)):
                i = len(self.minheap) - i - 1
                if(self.minheap[i] < self.minheap[i // 2]):
                    temp = self.minheap[i // 2]
                    self.minheap[i // 2] = self.minheap[i]
                    self.minheap[i] = temp

heap = MinHeap()
heap.build_heap([9, 5, 6, 2, 3])
heap.insert(1)
heap.insert(7)
print(heap.del_min())
print(heap.del_min())
