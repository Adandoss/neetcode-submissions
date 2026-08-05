# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        visited = {curr}
        while curr.next:
            curr = curr.next
            if curr in visited:
                return True
            visited.add(curr)
        return False
