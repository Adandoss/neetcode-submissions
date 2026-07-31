class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while True:
            two_sum = numbers[i] + numbers[j]
            if two_sum == target:
                return [i + 1, j + 1]
            if two_sum < target: i += 1
            else: j -= 1
        