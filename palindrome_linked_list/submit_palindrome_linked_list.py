from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data) -> None:
        new_node = ListNode(data)
        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data) -> None:
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


# Optional[ListNode]はListNodeのリストという意味ではない
def isPalindrome(head: Optional[ListNode]) -> bool:
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums == nums[::-1]


if __name__ == "__main__":
    # LinkedListを作成
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(2)
    l.append(2)
    # print(l.head.val)
    # print(l.head.next.val)
    # l.print()
    print(isPalindrome(l.head))

