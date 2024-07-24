# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        res = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        left = 0
        right = 2
        while right > left and right < len(arr):
            if arr[right] == 0:
                res.append(sum(arr[left+1:right]))
                left = right
                right += 2
            else:
                right += 1
        ans = ListNode(res[0])
        cur = ans
        for i in range(1, len(res)):
            new = ListNode(res[i])
            cur.next = new
            cur = new
        return ans