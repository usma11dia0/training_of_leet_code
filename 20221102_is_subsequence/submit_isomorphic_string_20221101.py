# question
# https://leetcode.com/problems/is-subsequence/

# answer
# https://qiita.com/KueharX/items/ddf57a3f819e70f7e61f

#教訓：forの二重ループではなくpointerを二つ使うと対応可能。


from xmlrpc.client import boolean


class Solution:
    def isSubsequence(self, s: str, t: str) -> boolean:
        pre = cur = 0
        while pre < len(s) and cur < len(t):
            if s[pre] == t[cur]:
                pre += 1
            cur +=1
        return len(s) == pre


if __name__ == "__main__":
    test = Solution()
    s = "abc"
    t = "ahbgdc"
    print(test.isSubsequence(s, t))
