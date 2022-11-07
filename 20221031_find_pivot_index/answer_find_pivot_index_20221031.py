# 得られた学び：for文内にさらにfor文(sum関数含む)があると計算量が膨大になりがち。for文を少なくする方法を考える。
#             合計値を最初に算出して、後から引いていく事でfor文の繰り返しを減らす。

# answer
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1

from typing import List

# question
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1


# result: Time Limit Exceeded
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == S - leftsum - x:
                return i
            leftsum += x
        return -1


if __name__ == "__main__":
    test = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(test.pivotIndex(nums))
