class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for d in details:
            phn = d[0:10]
            g = d[10]
            age = d[11:13]
            seat = d[13:15]

            if int(age) > 60:
                res += 1

        return res
