class Solution:
    def twoSum(self, nums, target):
        numList ={}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n

            if diff in numList:
                return (numList[diff],i)
            #target is not there so add current element in dictionary
            numList[n] = i


       

sol = Solution()
nums = [2,7,11,15]
target = 17
print(sol.twoSum(nums, target))



     

    

            
        
                
        

