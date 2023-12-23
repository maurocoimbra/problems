"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    # The idea here will be store each sum of values in tmp variable, this variable will work as a way to keep track of the local sum and also to
    # serve as a carry out to the next sums. 
    # The result of the local binary sum will be the modulus of the tmp variable by 2(Example: 1 + 1 + 0(carry out) = 2 -> 2 % 2 = 0)
    # The carry out of the local binary sum will be the floor division of the tmp variable by 2 (Example: 1 + 1 + 0(carry out) = 2 -> 2 // 2 = 1)
    
    def addBinary(self, a: str, b: str) -> str:
        pos_a = len(a) - 1
        pos_b = len(b) - 1
        result = ""
        tmp = 0

        while pos_a >=0 or pos_b >= 0 or tmp > 0:
            if pos_a >= 0:
                tmp += int(a[pos_a])
                pos_a -= 1
                
            if pos_b >= 0:
                tmp += int(b[pos_b])
                pos_b -= 1
            
            result = str(tmp % 2) + result
            tmp = tmp // 2
        
        return result

string_a = "110"
string_b = "011"
solution = Solution()
string = solution.addBinary(string_a, string_b)

print(string)