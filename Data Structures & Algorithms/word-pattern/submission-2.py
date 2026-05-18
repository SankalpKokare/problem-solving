class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()

        if len(pattern) != len(word):
            return False

        p2w = {}
        w2p = {}

        for c, w in zip(pattern, word):
            if c in p2w and p2w[c] != w:
                return False
            if w in w2p and w2p[w] != c:
                return False

            p2w[c] = w
            w2p[w] = c

        return True
