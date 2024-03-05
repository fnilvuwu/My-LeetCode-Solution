class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        for stone in stones:
            if stone in jewels:
                sum = sum + 1

        return sum
        