# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        res = 0
        first = head
        second = prev

        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res
