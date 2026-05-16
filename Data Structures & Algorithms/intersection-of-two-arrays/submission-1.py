class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniq = set(nums1)

        res = set()

        for n in nums2:
            if n in uniq:
                res.add(n)

        return list(res)
