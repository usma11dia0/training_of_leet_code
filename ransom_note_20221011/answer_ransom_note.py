from typing import List


def canConstruct(ransomNote: str, magazine: str) -> bool:
    for str in set(ransomNote):
        if magazine.count(str) < ransomNote.count(str):
            return False
    return True

if __name__ == "__main__":
    print("test")

