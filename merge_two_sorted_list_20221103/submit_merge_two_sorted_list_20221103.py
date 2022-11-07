# question
# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1

# 方針:
# https://zenn.dev/ike_pon/articles/44bff726aa8749f5317c 参照

from typing import Optional


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


# テスト用関数 単方向リストのlist1,list2を作成する。
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, val) -> None:
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, val) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def remove(self, val) -> None:
        current_node = self.head
        # データがあるかつ先頭が削除対象の場合
        if current_node and current_node.val == val:
            self.head = current_node.next
            current_node = None
            return
        # 先頭が削除対象ではない場合
        previous_node = None
        while current_node and current_node.val != val:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None


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

    # リストを直接テストデータとして利用する → ×
    # test = Solution()
    # list1 = [1, 2, 3]
    # list2 = [1, 2, 4]
    # test.mergeTwoLists(list1, list2)

    # 単方向リストのlist1,list2を作成してテストデータとみなす → ×
    # list1 = list2 = ListNode()
    # list1.val = 1
    # list1.next = 2
    # list1.next.val = 2
    # list1.next.next = 3
    # list1.next.next.val = 3
    # list1.next.next.next = None
    # print(list1)

    # print(test.mergeTwoLists(list1, list2))

    # 単方向リストのlist1,list2を作成してテストデータとみなす(Udemy Ver) → ×
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(1)
    list2.append(2)
    list2.append(4)
    # print(list1.print())
    # print(list2.print())
    test = Solution()
    print(test.mergeTwoLists(list1.head, list2.head).show())
