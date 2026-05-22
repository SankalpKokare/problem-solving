class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        n1 = set(nums1)
        n2 = set(nums2)

        not_in_n2 = set()
        not_in_n1 = set()

        for n in nums1:
            if n not in n2:
                not_in_n2.add(n)

        for n in nums2:
            if n not in n1:
                not_in_n1.add(n)

        return [list(not_in_n2), list(not_in_n1)]
