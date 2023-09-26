
# solved on my own

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        size = len(a)
        print(f"size equals {size}")
        print(f"a")

        for i in range(0, size):
            print(f"we compare {i} and {size-1-i} ")
            if(a[i] != a[size-1-i]):
                return False
        
        return True
    
sol = Solution()

print(sol.isPalindrome(121))
