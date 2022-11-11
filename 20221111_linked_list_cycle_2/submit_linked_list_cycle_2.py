# Question
# 解説 https://www.youtube.com/watch?v=Oz7-VlcTpSQ
# python code https://zhenyu0519.github.io/2020/06/08/lc142/

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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        _slow = head
        _fast = head

        while _slow and _fast:
            _slow = _slow.next
            _fast = _fast.next.next if _fast.next else None
            if _slow == _fast:
                break

        if not _slow or not _fast or _slow != _fast:
            return None
        _slow = head
        while _slow != _fast:
            _slow = _slow.next
            _fast = _fast.next
        return _slow


if __name__ == "__main__":
    data = ListNode()
    test_case = data.createLinkedList([1, 2, 3, 4, 5])
    test = Solution()
    print(test.middleNode(test_case).show())
