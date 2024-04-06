class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_substring = 0
        curr = []
        longest = 0
        
        for i in range(len(s)):
            for j in range(len(curr)):
                if s[i] == curr[j]:
                    curr = curr[j+1:]
                    break
            curr.append(s[i])
            longest = len(curr)
            max_substring = max(longest, max_substring)
        
        return max_substring
