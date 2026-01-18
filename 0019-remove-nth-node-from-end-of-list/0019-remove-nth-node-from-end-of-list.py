# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headTemp = head
        p = head
        i = 0
        while head:
            head = head.next
            if n < i:
                p = p.next
            i += 1
        if i == n:
            return headTemp.next
        p.next = p.next.next
        return headTemp
        