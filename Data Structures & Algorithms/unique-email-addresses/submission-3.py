class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for i in range(len(emails)):
            local, domain = emails[i].split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            e = local + domain
            res.add(e)

        return len(res)
