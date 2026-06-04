class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        w2p = {}
        p2w = {}

        for wp, pw in zip(words, pattern):
            if wp in w2p and w2p[wp] != pw:
                return False

            if pw in p2w and p2w[pw] != wp:
                return False

            p2w[pw] = wp
            w2p[wp] = pw

        return True
