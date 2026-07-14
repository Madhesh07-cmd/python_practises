#Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=b=0
        for i in nums:
            if i==1:
                a=a+1
                b=max(a,b)
            else:
               a=0
        return  b
s=Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))