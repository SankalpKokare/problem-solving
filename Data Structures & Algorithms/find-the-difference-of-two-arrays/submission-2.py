class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        r1 = []
        r2 = []
        for n in n1:
            if n not in n2:
                r1.append(n)

        for n in n2:
            if n not in n1:
                r2.append(n)

        return [r1, r2]
