"""
Problem Statement - 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example - 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Thought process

T1 
1. Check for index
2. If target - current element = next element then return the index of both the elements

issue with the above solution
1. We are only checking for the sum of consequtive elements
2. what is the sum element is at any other position in the array e.g [3,2,3] and target is 6

T2
1. Check for index
2. check_element = Target-current element 
3. check for the index of the element from step 2

"""

'''
# T1
class Solution(object):                                     # Define Class
    def twoSum(self, nums, target):                         # Define Function
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):                        # iterate through the array
            output = []                                     # list to store the output
            current_element = nums[i]                       # get the current element
            if (target - current_element) == nums[i+1]:     # check if target - current element is the next element
                output.append(i)                            # If yes append both to the output list
                output.append(i+1)
                break
            else:
                continue
        return output
'''  
# T2

# arr = [3,2,3]
# target = 6

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)-1):
#             current_element = nums[i]
#             required_element = target - current_element
#             try :
#                 required_index = nums.index(required_element,i+1)
#                 output = [i,required_index]
#                 break
#             except ValueError :
#                 continue
#         return output

num = [3,2,3]
target = 6

for index, value in enumerate(num):
    current_element = num[index]
    required_element = target - current_element
    try :
        required_index = num.index(required_element,index+1)
        output = [index,required_index]
        break
    except ValueError :
        continue
print(output)



# Ideal Solution
# This runs in O(n) time as iterating through a dict takes O(1)
num = [3,2,3]
target = 6

class Solution(object):
    def twoSum(self, nums, target):
        # We will create a dictionary to store the values
        store = {}
        for i in range(len(nums)):
            required_element = target - nums[i]
            if required_element in store:
                return [i,store[required_element]]
            store[nums[i]] = i
        return []
