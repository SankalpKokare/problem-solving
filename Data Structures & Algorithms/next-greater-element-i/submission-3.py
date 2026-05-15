class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        res = []

        for i, n in enumerate(nums2):
            hmap[n] = i

        for i, n in enumerate(nums1):
            res.append(-1)
            ind = hmap[n]
            for j in range(ind, len(nums2)):
                if nums2[j] > n:
                    res[-1] = nums2[j]
                    break

        return res
