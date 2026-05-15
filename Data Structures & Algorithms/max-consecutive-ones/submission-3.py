class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur_max = 0

        for n in nums:
            cur_max = cur_max + 1 if n == 1 else 0
            res = max(res, cur_max)

        return res
