class LinkedList:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.left = LinkedList(0, None, None)
        self.right = LinkedList(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        curr = LinkedList(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.size -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.value

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.value

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.size == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()