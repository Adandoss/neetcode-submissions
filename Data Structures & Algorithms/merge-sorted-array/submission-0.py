class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [0] * (m+n)
        i, j = 0, 0
        while i + j != n + m:
            if j >= n:
                result[i+j] = nums1[i]
                i += 1
            elif i >= m:
                result[i+j] = nums2[j]
                j += 1
            elif nums1[i] > nums2[j]:
                result[i + j] = nums2[j]
                j += 1
            else:
                result[i + j] = nums1[i]
                i += 1

        nums1[:] = result[:]

        