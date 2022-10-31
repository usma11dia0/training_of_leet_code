# 得られた学び：for文にてindexを一つ減らしたリストを活用することで、記載コード量を減らすことが出来る。
# 　　　　　　　リストのindex指定による要素更新に慣れる。


# answer
# https://leetcode.com/problems/running-sum-of-1d-array/discuss/2635285/Comprehensive-Python-Explanation-4-methods
from typing import List


class Solution:
    def runningSum1(self, nums: List[int]) -> List[int]:
        return print([sum(nums[: i + 1]) for i in range(len(nums))])

    def runningSum2(self, nums: List[int]) -> List[int]:
        runSum = [nums[0]]
        for i in range(1, len(nums)):
            runSum.append(runSum[i - 1] + nums[i])
        return runSum

    def runningSum3(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums


if __name__ == "__main__":
    test = Solution()
    test.runningSum1([3, 1, 2, 10, 1])
