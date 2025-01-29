class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            #skip non-alphanum
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                # Compare chharacters
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True