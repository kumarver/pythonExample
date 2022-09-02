''' Given an array of intergers and an interger k, you need to find the total number of
continuos subarray whose sum equals to k.'''

class Solution:
    def subarrSum(self, nums, target):
        sumdict = {0: 1}
        n = len(nums)
        count = 0
        s = 0
        for num in nums:
            #import pdb;pdb.set_trace()
            s += num
            if s - target in sumdict:
                #import pdb;pdb.set_trace()
                count = count + sumdict[s-target]
            if s in sumdict:
                sumdict[s] += 1
            else:
                sumdict[s] = 1
        print(sumdict)
        return count
    
nums = [1,4,3,-1,6,8,0,7]
target = 7
s = Solution()
print(s.subarrSum(nums, target))
