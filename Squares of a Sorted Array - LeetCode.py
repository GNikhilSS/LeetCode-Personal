class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = []
        for i in nums:
            squared_nums.append(i**2)

        result = []
        l = 0
        r = len(nums) - 1
        while l != r :
            if squared_nums[l] > squared_nums[r]:
                result.append(squared_nums[l])
                l += 1                
            else:
                result.append(squared_nums[r])
                r -= 1               
        
        result.append(squared_nums[r])
        return result[:: -1]
