class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        

class MyLinkedList:

    def __init__(self):
        self.head = Node()
    def get(self, index: int) -> int:
        n=0
        curr=self.head.next
        
        while curr and  n < index:
            curr=curr.next
            n+=1
        return curr.val if curr else -1
    def addAtHead(self, val: int) -> None:
        curr=Node(val)
        temp=self.head.next
        self.head.next=curr
        curr.next=temp
    def addAtTail(self, val: int) -> None:
        curr=Node(val)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=curr
        curr.next=None
    def addAtIndex(self, index: int, val: int) -> None:
        curr=Node(val)
        n=0
        temp=self.head
        while temp and n<index:
            temp=temp.next
            n+=1
        if not temp:
            return
        node=temp.next
        temp.next=curr
        curr.next=node
        
    def deleteAtIndex(self, index: int) -> None:
        n=0
        curr=self.head
        while curr and n<index:
            curr=curr.next
            n+=1
        if not curr or not curr.next:
            return
        curr.next=curr.next.next
        


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)