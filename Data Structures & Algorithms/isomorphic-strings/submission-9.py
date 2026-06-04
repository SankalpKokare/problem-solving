class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        st = {}
        ts = {}

        for sw, tw in zip(s, t):
            if sw in st and st[sw] != tw:
                return False

            if tw in ts and ts[tw] != sw:
                return False

            st[sw] = tw
            ts[tw] = sw

        return True
