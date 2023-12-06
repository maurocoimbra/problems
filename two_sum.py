"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    # The idea here is to use a hashmap with the values from the list and their respective indexes
    # Every time an element from the list is read the script checks if its complementary (the number that summed to it equals to the result)
    # already exists in the hashmap if so, their indexes are returned
    # After that, the element is added to the hashmap (it is important that this happens after so the script can work correctly when the complementary
    # number is the number itself)

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {} # {value : index}

        for i, num in enumerate(nums):
            if hashmap.get(target - num, None) != None:
                return [i, hashmap[target - num]]
            
            hashmap[num] = i

example = [2, 7, 11, 15]
target = 9

solution = Solution()
answer = solution.twoSum(example, target)
print(answer)