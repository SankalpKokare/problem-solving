class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur_max = 0

        for n in nums:
            if n != 1:
                cur_max = 0
                continue
            cur_max += 1
            res = max(cur_max, res)

        return res
