class Solution(object):
    def twoSum(self, nums, target):
        # First attempt
        # Empty dictionary created
        numToIndex = {}
        # loops through the list of numbers
        for i in range(len(nums)):
            # if the value of target - nums[i] is in the dictionary return the [index of the first number, 
            # index of the other number required]
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            # Adds current number to numToIndex with an index of i
            numToIndex[nums[i]] = i
        return []
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        #loop that iterates through each index i and number n in the nums list using the enumerate() function. 
        # This function returns both the index and the value of each element in the list. 
        for i, n in enumerate(nums):
            diff = target - n
            # If the difference is in the dictionary return [index of diff in prevMap, and current index]
            if diff in prevMap:
                return [prevMap[diff], i]
            # If not found add current number n into prevMap and have index value be i
            prevMap[n] = i