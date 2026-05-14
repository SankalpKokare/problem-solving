class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_cnt = defaultdict(int)

        for w in words:
            for c in w:
                char_cnt[c] += 1

        for c in char_cnt:
            if char_cnt[c] % len(words) != 0:
                return False

        return True
