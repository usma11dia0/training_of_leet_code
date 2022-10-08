from typing import List


def romanToInt(s: str) -> int:
    sum = 0
    count_roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    skip_flag = False
    for i, str_roman in enumerate(s):
        if skip_flag:
            skip_flag = False
            continue
        if i != len(s) - 1:
            if str_roman == "I" and s[i + 1] == "V":
                sum += 4
                skip_flag = True
            elif str_roman == "I" and s[i + 1] == "X":
                sum += 9
                skip_flag = True
            elif str_roman == "X" and s[i + 1] == "L":
                sum += 40
                skip_flag = True
            elif str_roman == "X" and s[i + 1] == "C":
                sum += 90
                skip_flag = True
            elif str_roman == "C" and s[i + 1] == "D":
                sum += 400
                skip_flag = True
            elif str_roman == "C" and s[i + 1] == "M":
                sum += 900
                skip_flag = True
            else:
                sum += count_roman[str_roman]
        else:
            sum += count_roman[str_roman]
    return sum


if __name__ == "__main__":
    test = "III"
    print(romanToInt(test))
