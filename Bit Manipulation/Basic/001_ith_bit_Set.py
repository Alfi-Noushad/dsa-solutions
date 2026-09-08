class solution:
    def check(self,n,i):
        mask = 1 << i
        return (n & mask) != 0

s = solution()
a = s.check(5,2)
print(a)