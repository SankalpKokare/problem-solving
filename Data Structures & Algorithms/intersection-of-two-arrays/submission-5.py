class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniq_n1 = set(nums1)
        uniq_n2 = set(nums2)

        res = set()

        for n in nums1:
            if n in uniq_n2:
                res.add(n)

        for n in nums2:
            if n in uniq_n1:
                res.add(n)

        return list(res)
