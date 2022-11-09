# Question https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createLinkedList(self, list: List):
        head = ListNode(list[0])
        p = head
        for i in list[1:]:
            p.next = ListNode(val=i)
            p = p.next
        return head

    def show(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return res


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target_node = count_node = head
        while count_node and count_node.next:
            target_node = target_node.next
            count_node = count_node.next.next
        return target_node


if __name__ == "__main__":
    data = ListNode()
    test_case = data.createLinkedList([1, 2, 3, 4, 5])
    test = Solution()
    print(test.middleNode(test_case).show())
