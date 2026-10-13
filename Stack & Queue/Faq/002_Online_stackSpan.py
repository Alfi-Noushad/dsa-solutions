class StockSpanner(object):

    def __init__(self):
        self.price = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.price and self.price[-1][0] <= price:
            self.price.pop()
            span += 1
        
        self.price.append(price,span)

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)