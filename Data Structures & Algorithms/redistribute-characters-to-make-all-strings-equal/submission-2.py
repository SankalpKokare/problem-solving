class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_total = defaultdict(int)
        for w in words:
            for c in w:
                count_total[c] += 1

        for c in count_total:
            if count_total[c] % len(words) != 0:
                return False
        return True
