"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def reverseString1(self, s: list[str]) -> None:
        # The idea here is to use a linked list to insert the elements in the head, and then updating the original list, not ideal 
        modified = []
        for char in s:
            modified.insert(0, char)
        s[:] = modified

    def reverseString2(self, s: list[str]) -> None:
        # The idea here is to exchange the left and right values progressively, better than the previous solution
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    def reverseString3(self, s: list[str]) -> None:
        # This method uses the built in list slicing from python to iterate throught the list from the ending to the beggining 
        s[:] = s[::-1]

    def reverseString4(self, s: list[str]) -> None:
        # This method uses the built in reverse function from python to reverse the list
        s.reverse()

# Test case
string = [*"ExamPle"]
solution = Solution()
solution.reverseString2(string)

print(string)