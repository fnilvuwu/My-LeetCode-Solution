class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric = ""
        for char in s:
            if char.isalnum():
                alphanumeric += char
        if alphanumeric == alphanumeric[::-1]:
            return True
        return False


        