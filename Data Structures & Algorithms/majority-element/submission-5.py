class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cur_res = 0

        for n in nums:
            if cur_res == 0:
                res = n
            cur_res += 1 if res == n else -1

        return res
