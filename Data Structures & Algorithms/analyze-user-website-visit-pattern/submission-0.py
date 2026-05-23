class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()

        mp = defaultdict(list)

        for t, u, s in arr:
            mp[u].append(s)

        count = defaultdict(int)

        for user in mp:
            patterns = set()
            cur_site = mp[user]
            print("cur", cur_site)
            for i in range(len(cur_site)):
                for j in range(i + 1, len(cur_site)):
                    for k in range(j + 1, len(cur_site)):
                        patterns.add((cur_site[i], cur_site[j], cur_site[k]))
                        print(f"add pattern for {user}", patterns)
            for p in patterns:
                count[p] += 1

        max_count = 0
        res = tuple()

        for pattern in count:
            if count[pattern] > max_count or (count[pattern] == max_count and pattern < res):
                max_count = count[pattern]
                res = pattern
        return list(res)
