class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        arr_result = [0] * n
        current_mod = 0

        for i in range(n):
            # I'm still confuse with this part
            current_mod = (current_mod * 10 + int(word[i])) % m

            if current_mod == 0:
                arr_result[i] = 1

        return arr_result