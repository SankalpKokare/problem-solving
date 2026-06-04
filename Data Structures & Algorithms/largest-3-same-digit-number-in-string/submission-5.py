class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] == num[i + 1]:
                res = max(res, num[i - 1 : i + 2])

        return str(res)
