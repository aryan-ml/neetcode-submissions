class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cn = 0
        # for i in s:
        #     if i in t:
        #         cn += 1
    
        # if cn == len(t):
        #     return True
        # else:
        #     return False

        return sorted(s) == sorted(t)