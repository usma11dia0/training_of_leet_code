# Question https://leetcode.com/problems/reverse-linked-list/solutions/?envType=study-plan&id=level-1&q=test&orderBy=most_relevant

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return res

    def createLinkedList(self, list: List):
        head = ListNode(val=list[0])
        # headと混合しないよう別名で変数を定義
        p = head
        for i in list[1:]:
            p.next = ListNode(val=i)
            p = p.next
        return head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node:
            # 順番を入れ替える処理
            # 現時点の次のnodeを一時的にnext_node内へ保管
            next_node = current_node.next
            # 現時点の次を前のnodeに指定
            current_node.next = previous_node

            # 前のnodeとして現時点のnodeを指定
            previous_node = current_node
            # 現時点のnodeとして次のnodeを指定
            current_node = next_node

        head = previous_node
        return head


if __name__ == "__main__":
    data = ListNode().createLinkedList([1, 2, 3])
    # print(data.show())
    test = Solution()
    print(test.reverseList(data).show())
