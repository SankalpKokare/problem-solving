class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        countText = Counter(text)
        countBalloon = Counter("balloon")

        res = len(text)

        for key in countBalloon:
            res = min(countText[key] // countBalloon[key], res)

        return res
