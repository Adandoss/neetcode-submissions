class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def enqueue(self, val) -> None:
        new_node = ListNode(val=val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def dequeue(self) -> int | None:
        
        if self._size == 0:
            return None
        elif self._size == 1:
            value = self.head.val
            self.head = None
            self.tail = None
        else:
            value = self.head.val
            self.head = self.head.next

        self._size -= 1

        return value

    def peek(self) -> int | None:
        if self._size != 0:
            return self.head.val

    @property
    def size(self) -> int:
        return self._size

class MyStack:

    def __init__(self):
        self.size = 0
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    def push(self, x: int) -> None:
        if self.queue_2.size > 0:
            self.queue_2.enqueue(x)
        else:
            self.queue_1.enqueue(x)
        
        self.size += 1

    def pop(self) -> int | None:
        if self.queue_1.size + self.queue_2.size == 0:
            return None

        filled_queue = self.queue_1 if self.queue_1.size != 0 else self.queue_2
        empty_queue  = self.queue_1 if self.queue_1.size == 0 else self.queue_2

        for i in range(filled_queue.size - 1):
            empty_queue.enqueue(filled_queue.dequeue())

        self.size -= 1

        return filled_queue.dequeue()
        
    def top(self) -> int | None:
        if self.queue_1.size + self.queue_2.size == 0:
            return None

        filled_queue = self.queue_1 if self.queue_1.size != 0 else self.queue_2
        empty_queue  = self.queue_1 if self.queue_1.size == 0 else self.queue_2

        for i in range(filled_queue.size - 1):
            empty_queue.enqueue(filled_queue.dequeue())

        top_val = filled_queue.dequeue()
        empty_queue.enqueue(top_val)

        return top_val

    def empty(self) -> bool:
        return not self.size


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()