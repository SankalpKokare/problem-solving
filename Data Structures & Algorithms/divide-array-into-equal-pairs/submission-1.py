class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        countN = Counter(nums)

        for v in countN.values():
            if v % 2 == 1:
                return False

        return True
