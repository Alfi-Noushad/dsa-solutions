class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack=[]
        output = []
        next_greater ={}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            output.append(next_greater.get(num,-1))
        return output


        







'''
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        output = []
        
        for num in nums1:
            found = False
            for i in range(len(nums2)):
                if num == nums2[i]:
                    for j in range(i+1,len(nums2)):
                        if nums2[j] > num:
                            output.append(nums2[j])
                            found = True
                            break
                    if not found:
                        output.append(-1)

        return output


'''