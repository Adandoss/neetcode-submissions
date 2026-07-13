class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        return [x[0] for x in num_counts.most_common(k)]