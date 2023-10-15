
# done by myself and it works
# but won't pass the leetcode test

nums = [2,3,2,3,3,6,6,7,2,2,2,2,2]

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        value = 0
        freq = 0
        maxFreq = 0
        maxFreqValue = 0
        n = len(nums)

        for i in range(n):
            value = nums[i]
            freq = 1
            for j in range(i+1,n):
                if value == nums[j]:
                    freq += 1
                    if freq > maxFreq:
                        maxFreq = freq
                        maxFreqValue = nums[i]
            
        if maxFreq > n/2:
            return maxFreqValue
        
sol = Solution()

print(sol.majorityElement(nums))