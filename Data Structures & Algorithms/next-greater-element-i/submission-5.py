class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_idx = {}
        res = []

        for i, n in enumerate(nums2):
            num_idx[n] = i

        for i in range(len(nums1)):
            res.append(-1)
            if nums1[i] in num_idx:
                for j in range(num_idx[nums1[i]], len(nums2)):
                    if nums2[j] > nums1[i]:
                        res[-1] = nums2[j]
                        break

        return res
