class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size: 
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val=val)
        new_node.next = self.head
        self.head = new_node

        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
            
        new_node = ListNode(val=val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        if index == 0:
            self.addAtHead(val=val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        new_node = ListNode(val=val)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return

        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        if index == self.size - 1:
            self.tail = prev_node

        prev_node.next = prev_node.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)