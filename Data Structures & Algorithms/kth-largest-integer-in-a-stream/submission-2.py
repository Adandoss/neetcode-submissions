class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = [-sys.maxsize] * (k+1)
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
        while 2 * i < len(self.minheap):
            left = 2 * i
            right = 2 * i + 1
            smaller_child = left
            
            if right < len(self.minheap) and self.minheap[right] < self.minheap[left]:
                smaller_child = right
            
            if self.minheap[i] > self.minheap[smaller_child]:
                self.minheap[i], self.minheap[smaller_child] = self.minheap[smaller_child], self.minheap[i]
                i = smaller_child
            else:
                break
