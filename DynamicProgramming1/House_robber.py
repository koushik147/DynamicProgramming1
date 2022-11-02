#Time_Complexity: O(n) 
#Space_Complexity : O(n)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: # array length is one
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1]) # array length is two
        firstprev = nums[0] # assigning value to firstprev pointer
        secondprev = max(nums[0],nums[1]) # assigning the max between first two values to secondprev pointer
        for i in range(2,len(nums)): 
            curr = max(secondprev,firstprev + nums[i]) # assigning the max value between first+i and second to curr pointer
            firstprev=secondprev # assigning second to first
            secondprev=curr # assigning to curr to second
        return curr # returning curr
