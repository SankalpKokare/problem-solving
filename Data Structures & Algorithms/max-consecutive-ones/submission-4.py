class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur_count = 0

        for n in nums:
            if n == 1:
                cur_count += 1
            else:
                cur_count = 0

            res = max(cur_count, res)

        return res
