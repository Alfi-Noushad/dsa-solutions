class Solution(object):
    def countSubsting(self, s,k):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        answer = 0
        freq = {}
        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            answer += right - left + 1
            right += 1
            
        return answer

s = Solution()
a =s.countSubsting("aba",3)
print(a)











'''

class Solution(object):
    def countSubsting(self, s,k):
        """
        :type s: str
        :rtype: int
        """
        count =0
        freq = {}
        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):
                if s[j] not in freq:
                    freq[s[j]] = 1
                else:
                    freq[s[j]] += 1
                if len(freq) == k:        
                    count += 1
                elif len(freq) > k:
                    break
        return count

s = Solution()
a =s.countSubsting("abcd",2)
print(a)

'''
        