class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Changed to a default dict because lists cannot be used as key. so instead tuples are used
        # default values being the list 
        res = defaultdict(list)

        # Iterates through each string in strs
        for s in strs:
            # Initialize a list of value 0 26 times for each letter in the alphabet
            count = [0] * 26

            # Iterates through every character in each string
            for c in s:
                # gets the ascii value of each character in the string subtracting the ascii value of a
                # This gives the index within count so b = 81 - 80 = index 1
                count[ord(c) - ord("a")] += 1

            # Convert the count list to a tuple to use as a key in the defaultdict
            # Append the current string to the list corresponding to the count tuple key
            res[tuple(count)].append(s)

        return res.values()