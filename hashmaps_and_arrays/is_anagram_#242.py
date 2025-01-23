class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {}

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            set1[s[i]] = set1.get(s[i], 0) + 1
            set2[t[i]] = set2.get(t[i], 0) + 1

    
        return set1 == set2
       
