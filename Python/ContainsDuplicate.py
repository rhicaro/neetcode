class Solution(object):
    # First attempt
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numLength = len(nums)
        nums.sort()
        for x in nums:
            for y in range(numLength):
                if (x == nums[y+1]):
                    return True
                else:
                    return False
               
    # Best Solution
    def containsDuplicate2(self, nums):
        # creates a new set
        hashset = set()


        # iterates through elements in nums
        for n in nums:
            # if n is in that set then return true
            if n in hashset:
                return True
            # if n isnt found in that set, the set adds n
            hashset.add(n)
            # if it goes through the entirety of the for loop it returns false
        return False
