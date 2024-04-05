class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def stretchy(word: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False
                
                count_s = 1
                while i + 1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    count_s += 1
                
                count_w = 1
                while j + 1 < len(word) and word[j] == word[j+1]:
                    j += 1
                    count_w += 1
                
                if count_s < 3 and count_s != count_w:
                    return False
                if count_s >= 3 and count_s < count_w:
                    return False
                
                i += 1
                j += 1
            
            return i == len(s) and j == len(word)
        
        count_stretchy = 0
        for word in words:
            if stretchy(word):
                count_stretchy += 1
        
        return count_stretchy