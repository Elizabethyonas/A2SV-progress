# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pivot = slow
        prev = None
        while pivot:
            temp=pivot.next
            pivot.next=prev
            prev=pivot
            pivot=temp
        if head.val != prev.val:
            return False
        while prev and prev.next:
            prev = prev.next
            head = head.next
            if prev.val != head.val:
                return False
        return True

        