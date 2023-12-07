"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    # The idea here will be to create a hashmap with the characters for keys and the number of their occurrences for values with the first strin
    # Then the algorithm will starting subtracting from the hashmap as the second string is read, if it is all null in the end, return True
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {} # {char : n_occurrences}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for char in t:
            hashmap[char] = hashmap.get(char, 0) - 1
            if hashmap[char] < 0:
                return False

        for value in hashmap.values():
            if value != 0:
                return False

        return True

test_case1 = "rat"
test_case2 = "tar"

solution = Solution()
answer = solution.isAnagram(test_case1, test_case2)

print(answer)