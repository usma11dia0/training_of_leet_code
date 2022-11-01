# question
# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1

# 方針：文字列内の異なる文字数を比較。
#      例：[b,a,b,a]の場合、2を出力する。
#         1.結果格納リストを作成
#      　 2.リスト内の要素をfor文で取り出す
#         3.取り出した要素が格納リストになければ追加。もしあれば追加しない。
#         4.すでに格納されていた場合はbreakでfor文ループから抜け出す。

# Wrong Answer 同じ文字で二つの文字を置き換えることが出来ないため、方針自体が誤り。
class Solution:
    def isIsomorphic(self, s: str, t: str) -> int:
        s_char_list = []
        t_char_list = []
        for s_char in s:
            append_flag = False
            if len(s_char_list) == 0:
                s_char_list.append(s_char)
            else:
                for s_list_char in s_char_list:
                    if s_char != s_list_char:
                        append_flag = True
                    else:
                        append_flag = False
                        break
                if append_flag == True:
                    s_char_list.append(s_char)
        for t_char in t:
            append_flag = False
            if len(t_char_list) == 0:
                t_char_list.append(t_char)
            else:
                for t_list_char in t_char_list:
                    if t_char != t_list_char:
                        append_flag = True
                    else:
                        append_flag = False
                        break
                if append_flag == True:
                    t_char_list.append(t_char)
        return len(s_char_list) == len(t_char_list)


if __name__ == "__main__":
    test = Solution()
    s = "bbbaaaba"
    t = "aaabbbba"
    print(test.isIsomorphic(s, t))
