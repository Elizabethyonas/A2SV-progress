# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev_node = head
        if prev_node.next:
            current_node = prev_node.next
            prev_node.next = None
            if current_node.next:
                next_node = current_node.next
            else:
                next_node = None
        else:
            return prev_node

        while next_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = prev_node
        return current_node
        