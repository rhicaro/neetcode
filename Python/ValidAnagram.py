class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # First take
        if len(s) != len(t):
            return False
        
        sCounts, tCounts = {}, {}

        for x in s:
            if x in sCounts:
                sCounts[x] += 1
            else:
                sCounts[x] = 1

        for y in t:
            if y in tCounts:
                tCounts[y] += 1
            else:
                tCounts[y] = 1

        return sCounts == tCounts
    
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Best solution
        # if the length isnt the same then return False
        if len(s) != len(t):
            return False
        
        # Instantiate 2 dictionaries
        sCounts, tCounts = {}, {}

        # repeat through whatever number of letters in the string
        for i in range(len(s)):
            # increments the count of the character s[i] in string s by 1. If the character is not already present in countS/T, 
            # it initializes its count to 1 using the get() method. 
            # Otherwise, it retrieves its current count and increments it by 1.
            sCounts[s[i]] = 1 + sCounts.get(s[i], 0)
            tCounts[t[i]] = 1 + tCounts.get(t[i], 0)

        # If the two dictionaries are the same then return true else return false
        return sCounts == tCounts