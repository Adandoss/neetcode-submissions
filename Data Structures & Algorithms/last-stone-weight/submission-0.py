class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            num1 = heapq.heappop(max_heap)
            num2 = heapq.heappop(max_heap)
            if num1 == num2:
                continue
            else:
                heapq.heappush(max_heap, (num1 - num2))
            
        return -1*max_heap[0] if len(max_heap) else 0

