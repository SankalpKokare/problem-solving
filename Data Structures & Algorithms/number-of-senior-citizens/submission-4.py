class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for d in details:
            phn_no = d[:10]
            g = d[10:11]
            age = d[11:13]
            if int(age) > 60:
                res += 1

        return res
