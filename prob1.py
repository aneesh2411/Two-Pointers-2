class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 1
        count = 1
        j = 1
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]):
                count = count +  1
            else:
                count = 1
        
            if(count <=2):
                nums[j] = nums[i]
                j =j + 1
            
        return j