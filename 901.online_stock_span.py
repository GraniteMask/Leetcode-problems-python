# Brute Force Method
class StockSpanner:

    def __init__(self):
        self.q = collections.deque()  # pair: [price, span]

    def next(self, price: int) -> int:
        if len(self.q) == 0:
            self.q.append([price, 1])
            return self.q[-1][1]
        else:
            if self.q[-1][0] <= price:
                temp = 1
                while self.q and self.q[-1][0] <= price:
                    p, span = self.q.pop()
                    temp += span
                self.q.append([price, temp])
                
                
            else:
                self.q.append([price, 1])
            print(self.q)
            return self.q[-1][1]



# More Optimized Version of above code

class StockSpanner:

    def __init__(self):
        self.q = collections.deque()  # pair: [price, span]

    def next(self, price: int) -> int:
        temp = 1
        while self.q and self.q[-1][0] <= price:
            p, span = self.q.pop()
            temp += span
        self.q.append([price, temp])


        return self.q[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)