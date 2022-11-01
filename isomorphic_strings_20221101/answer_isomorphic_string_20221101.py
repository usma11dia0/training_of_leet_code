# answer
# https://leetcode.com/problems/isomorphic-strings/solution/

# 学び：文字列の中に要素が含まれているかどうかは、x not in yで対応可能
#       マッピングのように1対1関係を示すには辞書型を用いるのがよい。


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True


if __name__ == "__main__":
    test = Solution()
    s = "bbbaaaba"
    t = "aaabbbba"
    print(test.isIsomorphic(s, t))
