"""
2129. Capitalize the Title
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.
"""

class Solution:
    # The idea here will be to split the input string using blank spaces, checking the length of each sub string and then correcting the capitalization
    # Since it isn't possible to reassing elements from a string using indexes (string[0] = string[0].upper()) a new variable is needed
    def capitalizeTitle(self, title: str) -> str:
        splitted = title.split()
        answer = ""

        for word in splitted:
            if len(word) <= 2:
                answer += word.lower()
            else:
                answer += word[0].upper()
                answer += word[1:].lower()
            answer += " "
        
        return answer[:-1]

test_case = "capiTalIze tHe titLe"

solution = Solution()
answer = solution.capitalizeTitle(test_case)

print(answer)