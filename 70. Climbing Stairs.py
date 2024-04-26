class Solution:
    def climbStairs(self, n: int) -> int:
        # basically sum of fibonacci at n
        if n <= 2:
            return n
        
        prev1, prev2 = 1, 2
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        
        return prev2
        
