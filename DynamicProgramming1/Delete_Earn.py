class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = [0]*(max(nums)+1) # defining freq matrix
        for i in nums:
            freq[i] += i # adding i in matrix
            
        if len(freq) == 1:
            return [0]
        profit = freq[0] # assigning first to profit
        curr_profit = freq[1] # assigning second to curr_pointer
        for i in range(2, len(freq)):
            if (freq[i] + profit) > curr_profit: # if ith value + previous profit is greater than current profit
                temp = curr_profit # assigning current profit to temp
                curr_profit = profit + freq[i] # assignning ith value + previous profit to current profit
                profit = temp # assigning temp to profit
            else:
                profit = curr_profit
                
        return curr_profit # returning current profit