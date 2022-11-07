# 得られた学び：for文を降順(後→前)で回すことで、問題が簡単になる場合がある。
# 　　　　　　　辞書型の定義に慣れる。


# answer
# https://leetcode.com/problems/roman-to-integer/discuss/450264/Python-Beginner-98-fast-100-Memo


def romanToInt(s: str) -> int:
    res, prev = 0, 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in s[::-1]:  # rev the s
        if dict[i] >= prev:
            res += dict[i]  # sum the value if previous value same or more
        else:
            res -= dict[
                i
            ]  # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
        prev = dict[i]
    return res


if __name__ == "__main__":
    test = "MCMXCIV"
    print(romanToInt(test))
