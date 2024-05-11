class Solution:
    # First Attempt
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = res + " " + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        res = s.split(" ")
        res.pop(0)
        return(res)
    
    # Best attempt
    def encode(self, strs):
        # Creates an empty string
        res = ""
        # Iterates through the array
        for s in strs:
            # Adds 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res