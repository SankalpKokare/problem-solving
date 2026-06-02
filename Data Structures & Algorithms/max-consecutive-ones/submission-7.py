class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_count = 0
        res = 0

        for n in nums:
            if n == 1:
                cur_count += 1
            else:
                cur_count = 0

            res = max(res, cur_count)

        return res
