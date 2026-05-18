class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        countBalloon = Counter("balloon")

        res = len(text)

        for k in countBalloon.keys():
            res = min(countText[k] // countBalloon[k], res)

        return res
