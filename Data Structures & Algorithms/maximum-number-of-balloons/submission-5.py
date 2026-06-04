class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        countText = Counter(text)
        countBalloon = Counter("balloon")
        res = float("inf")

        for c in countBalloon:
            count = countText[c] // countBalloon[c]
            res = min(count, res)

        return res
