class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m-1
        r = n-1

        while min(l, r) >= 0:
            if nums1[l] > nums2[r]:
                nums1[l+r+1] = nums1[l]
                l -= 1
            else:
                nums1[l+r+1] = nums2[r]
                r -= 1

        nums1[:r+1] = nums2[:r+1]        

