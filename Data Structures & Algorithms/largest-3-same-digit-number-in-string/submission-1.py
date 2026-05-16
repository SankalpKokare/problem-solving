class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                res = max(num[i - 2 : i + 1], res)

        return res
