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



class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = Queue()
        for stud in students:
            queue.enqueue(stud)

        sandwitch_index = 0
        rotations = 0

        while queue.size > 0 and rotations < queue.size:
            if queue.peek() == sandwiches[sandwitch_index]:
                queue.dequeue()
                sandwitch_index += 1
                rotations = 0
            else:
                queue.enqueue(queue.dequeue())
                rotations += 1

        return queue.size




