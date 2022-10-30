from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 回答格納用リスト
        answer = []
        # ループ数カウンター
        counter = 0
        for i in nums:
            if counter == 0:
                target = i
                answer.append(target)
                counter += 1
                tmp = target
            else:
                target = tmp + i
                answer.append(target)
                counter += 1
                tmp = target
        return print(answer)


if __name__ == "__main__":
    test = Solution()
    test.runningSum([3, 1, 2, 10, 1])
