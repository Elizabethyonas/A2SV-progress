# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodes = 0
        curr = head
        ans = [None] * k
        while curr:
            curr = curr.next
            nodes += 1
        splits = nodes // k
        extra = nodes % k
        curr = head
        for i in range(k):
            ans[i] = curr
            if not curr:
                continue
            for j in range(splits - 1 + (1 if extra else 0)):
                curr = curr.next
            if extra > 0:
                extra -= 1
            temp = curr.next
            curr.next = None
            curr = temp
        return ans