class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        countHeightFreq = Counter(heights)

        expected_height = []

        for i in range(1, 101):
            f = countHeightFreq[i]
            for _ in range(f):
                expected_height.append(i)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected_height[i]:
                res += 1

        return res
