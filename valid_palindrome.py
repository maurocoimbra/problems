"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    # The idea here is to first format the string (remove all non alphanumerical chars and empty spaces) and then
    # compare the chars from the most left and right indexes until reaching the middle
    # The only difference in the functions will be how those non alphanumerical characters will be removed

    # Using the re lib for regular expressions
    def isPalindrome1(self, s: str) -> bool:
        import re
        
        # \W matches any non word characters using regular expressions (the + allows for multiple occurrences of 
        # the pattern to be detected at once, making the operation more time efficient if multiple occurrences of those
        # chars are appearing consecutively)
        # Obs: "_" is also considered a word character, so to remove it as well we need to use an expression like this [\W_]
        s = re.sub("[\W_]+", "", s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
    
    # Using python built in isalnum() to remove undesired characters, slightly less time efficient
    def isPalindrome2(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()

        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

test_case = "ab_a"

solution = Solution()
answer = solution.isPalindrome1(test_case)

print(answer)