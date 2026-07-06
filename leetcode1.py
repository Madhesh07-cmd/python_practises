#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


class Solution(object):
    nums=[2,7,11,15]
    target=9
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        a=nums
        for i in range(0,len(a)-1):
            for j in range(i+1,len(a)):
                if a[i] + a[j] == target:
                    return i,j
s=Solution()
print(s.twoSum([2,7,11,15],9))
