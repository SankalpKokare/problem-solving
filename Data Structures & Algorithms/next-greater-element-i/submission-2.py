class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h_map = {}
        res = []

        for i in range(len(nums2)):
            if nums2[i] not in h_map:
                h_map[nums2[i]] = i

        for n in nums1:
            index = h_map[n]
            res.append(-1)
            for i in range(index, len(nums2)):
                if nums2[i] > n:
                    res[-1] = nums2[i]
                    break
        return res
