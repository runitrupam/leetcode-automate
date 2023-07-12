'''class Solution:
    def totalFruit(self, F: List[int]) -> int:
        n = len(F)
        if n <= 2:
            return n
        start = 0
        dp = dict()
        dp[F[0]] = 1
        res = 1
        for i in range(1,n):
            ch = F[i]
            if ch in dp and dp[ch] > 0:
                dp[ch] += 1

            elif len(dp.keys()) <= 1:
                dp[ch] = 1
            elif len(dp.keys()) == 2:
                ch_to_remove = F[start]
                # total_count_to_remove = dp[  ch_to_remove ]
                while(start < i  and len(dp.keys()) == 2 ):
                    dp[ F[start] ] -= 1
                    if dp[ F[start] ] == 0:
                        del dp[ F[start]] # pop the elment not used.
                    start += 1
                dp[ch] = 1
                # print(start,i,dp)
            curr_ln = 0
            for j in dp.keys():
                curr_ln += dp[j]
            res = max(res,curr_ln)
            # print(i,dp)
        return res
'''
class Solution:
  def totalFruit(self, tree: List[int]) -> int:
    ans = 0
    count = collections.defaultdict(int)

    l = 0
    for r, t in enumerate(tree):
      count[t] += 1
      while len(count) > 2:
        count[tree[l]] -= 1
        if count[tree[l]] == 0:
          del count[tree[l]]
        l += 1
      ans = max(ans, r - l + 1)

    return ans