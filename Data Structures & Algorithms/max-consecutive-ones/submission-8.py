class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_index = 0
        res = 0

        for n in nums:
            if n == 1:
                cur_index += 1
            else:
                cur_index = 0

            res = max(cur_index, res)

        return res
