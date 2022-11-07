# question
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
from typing import List

# question
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1


# result: Time Limit Exceeded
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        max_len = len(nums)
        for i in range(0, max_len):
            if sum(nums[:i]) == sum(nums[i + 1 :]):
                return i
        return -1


if __name__ == "__main__":
    test = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(test.pivotIndex(nums))
