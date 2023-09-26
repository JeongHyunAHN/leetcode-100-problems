class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prev = 0
        current = 0

        for i in range(len(nums)):
            current += nums[i]

            if(current < 0):
                current = 0

            if(prev < current):
                prev = current
        
        return prev
    
sol = Solution()

print(sol.maxSubArray([1,2,-1,5,3]))