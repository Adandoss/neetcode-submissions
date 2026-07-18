class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = [-9999] * (k+1)
        for n in nums:
            if n < self.minheap[1]: continue
            self.add_to_heap(n)

    def add(self, val: int) -> int:
        if val < self.minheap[1]: return self.minheap[1]
        self.add_to_heap(val)
        return self.minheap[1]

    def add_to_heap(self, val: int):
        self.minheap[1] = val
        i = 1
        while 2*i < len(self.minheap):
            if 2*i + 1 < len(self.minheap) and \
                self.minheap[2*i + 1] < self.minheap[2*i] and \
                self.minheap[i] > self.minheap[2*i + 1]:

                self.minheap[i], self.minheap[2*i + 1] = self.minheap[2*i + 1], self.minheap[i]
                i = 2*i + 1
            elif self.minheap[i] > self.minheap[2*i]: 
                self.minheap[i], self.minheap[2*i] = self.minheap[2*i], self.minheap[i]
                i = 2*i
            else:
                break
