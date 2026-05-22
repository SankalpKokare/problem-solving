class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        n1 = set(nums1)

        for n in nums2:
            if n in n1:
                res.add(n)

        return list(res)
