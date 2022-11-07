from typing import List


def canConstruct(ransomNote: str, magazine: str) -> bool:
    i = 1
    t = 0
    # ransom_list = [r for r in ransomNote]
    # magazine_list = [m for m in magazine]
    ransom_set = set([])
    for r in ransomNote:
        if ransom_set >= set(r):
            r = r + f"_{i}"
            ransom_set.add(r)
            i += 1
        else:
            ransom_set.add(r)

    # f_1がなぜか部分集合と見做されずwhile文を抜け、addに向かうも要素が被っているので付与されない。
    magazine_set = set([])
    for m in magazine:
        if set(m).issubset(magazine_set):
            while set(m).issubset(magazine_set):
                t += 1
                m = m + f"_{str(t)}"
            magazine_set.add(m)
        else:
            magazine_set.add(m)
        t = 0

    print(ransom_set)
    print(magazine_set)

    return magazine_set.issuperset(ransom_set)


if __name__ == "__main__":
    print(canConstruct("fffbfg", "effjfggbff"))


# "effjfggbffjdgbjjhhdegh"
