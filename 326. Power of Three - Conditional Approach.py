class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        log_n = math.log(n, 3)

        return abs(log_n - round(log_n)) < 1e-10