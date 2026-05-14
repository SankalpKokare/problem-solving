class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        val = 0

        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] == num[i + 1]:
                tmp = num[i - 1 : i + 2]

                if val <= int(tmp):
                    val = int(tmp)
                    res = tmp

        return res
