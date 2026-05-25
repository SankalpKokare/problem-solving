class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        countHeight = Counter(heights)

        expected = []

        for i in range(1, 101):
            c = countHeight[i]

            for _ in range(c):
                expected.append(i)

        res = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res
