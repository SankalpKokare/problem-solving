class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {}
        res = []

        for i, n in enumerate(nums2):
            index_map[n] = i

        for i in range(len(nums1)):
            index = index_map[nums1[i]]
            res.append(-1)
            for j in range(index, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[-1] = nums2[j]
                    break
        return res
