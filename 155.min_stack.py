class MinStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, val: int) -> None:
        self.q.append(val)

    def pop(self) -> None:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return min(self.q)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()