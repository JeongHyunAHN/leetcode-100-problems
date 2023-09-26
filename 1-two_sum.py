
# solved on my own

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                    return [i,j]
        

list = [1,3,5,7]
target = 254

print(twoSum(list,target))
