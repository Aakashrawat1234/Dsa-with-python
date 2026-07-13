class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i=0
        output=[]
        while i<len(nums):
            count=0
            j=0
            while j<len(nums):
                if(nums[j]<nums[i]):
                    count+=1
                j+=1     
            output.append(count)
            i+=1    
        return output           



