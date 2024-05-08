class Solution(object):
    def topKFrequent(self, nums, k):
        # First attempt
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = {}
        anwser = []

        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1

        # res.items(): This method returns a view object that displays a list of a dictionary's key-value pairs as tuples. So, res.items() will give us a list of tuples where each tuple 
        # contains a key-value pair from the dictionary res.

        # sorted(): This is a built-in function in Python that sorts any iterable object, such as lists, tuples, or in this case, the list of key-value pairs returned by res.items().

        # key=lambda x: x[1]: This specifies a custom sorting key. Here, we are using a lambda function to extract the second element (the value) from each tuple (x[1]). 
        # This tells the sorted() function to sort the list of tuples based on the values.
        sortedRes = sorted(res.items(), key=lambda x: x[1])

        count = 0
        for key in sortedRes:
            anwser.append(key)
            count += 1
            if count == k:
                break

        return anwser
    
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Dictionary is initialized
        count = {}
        # Nested Array is initialized where the other array is of range len of nums + 1
        freq = [[] for i in range(len(nums) + 1)]

        # Count the occurrences of each element in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Store elements in freq list based on their counts
        for n, c in count.items():
            freq[c].append(n)

        # Initialize an empty list to store the result
        res = []

        # Iterate over freq list in reverse order to get elements with highest frequency first
        for i in range(len(freq) - 1, 0, -1):
            # Iterate over elements in freq[i] list
            for n in freq[i]:
                # Append element to result list
                res.append(n)
                # If length of result list reaches k, return result
                if len(res) == k:
                    return res