class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = defaultdict(int)
        for n in nums:
            counts_dict[n] += 1

        result_list = []

        for _ in range(k):
            top_key = max(counts_dict, key=counts_dict.get)
            result_list.append(top_key)
            counts_dict.pop(top_key)

        return result_list