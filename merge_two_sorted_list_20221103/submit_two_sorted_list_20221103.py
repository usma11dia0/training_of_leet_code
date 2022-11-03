# question
# https://leetcode.com/study-plan/leetcode-75/?progress=x26sbvih

# 方針:
# https://zenn.dev/ike_pon/articles/44bff726aa8749f5317c 参照

# Wrong Answer 同じ文字で二つの文字を置き換えることが出来ないため、方針自体が誤り。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = res = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        dummy.next = list1 or list2

        return res.next


if __name__ == "__main__":
    test = Solution()
    list1 = [1, 2, 3]
    list2 = [1, 2, 4]
    print(test.mergeTwoLists(list1, list2))
