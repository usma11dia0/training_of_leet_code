from typing import Optional


class ListNode:
    def __init__(self, val, next=None) -> None:
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

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.val, end=" ")
            current_node = current_node.next


def isPalindrome(head: Optional[ListNode]) -> bool:
    fast = slow = head

    # ノードの長さが不明な中で左半分と右半分のノードに分けるには
    # fast, slowの二つのポインターを用意する
    # fastは１ステップで２ノード進む
    # slowは１ステップで１ノード進む でループ処理
    # ループ終了後ノードの中間点にslowのポインターが位置

    # 奇数の時　(whileループ2回 slow=2)
    # 1 2 3 4 5
    # f
    #     f
    #         f

    # 偶数の時
    # 1 2 3 4 5 6 none    の時(whileループ3回 slow=3)
    # f
    #     f
    #         f
    #             f

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # slowポインタ(中間点)以降を反転させたR(LinkedList)を新規作成する
    R = None
    while slow:
        nxt = slow.next  # slowポインタの次要素を取得
        slow.next = R  # 取得した次要素をRへ入れる
        R = slow  # slowへslow.next(R)を入れる
        slow = nxt  # slowポインタを次へ移動

    while R:
        if R.val != head.val:
            return False
        R = R.next
        head = head.next
    return True


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(3)
    l.append(2)
    l.append(1)
    # l.print()
    isPalindrome(l.head)

