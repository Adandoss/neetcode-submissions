class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(val=homepage)
        print("init: ", self.curr.val)

    def visit(self, url: str) -> None:
        new_node = ListNode(val=url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node        

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev and i != steps:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next and i != steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)