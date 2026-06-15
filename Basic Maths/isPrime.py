class Solution:
    def isPrime(self, n):
        count = 0
        for i in range(2,(n//2)+1):  #(n ** 0.5)
            if n % i == 0:
                count += 1
        return count
        

s = Solution()
result = s.isPrime(7)

if result:
    print("Not prime")
else:
    print("Prime")

#TC: O(n)
#SP: O(1)