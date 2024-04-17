class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        if len(s) != len(t):
            return False

        for i in s:
            try:
                rm = t.index(i)
                t.remove(i)
            except:
                return False

        return True