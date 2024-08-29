class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []; // Create an empty stack to store opening brackets
        const pairs = { // Define the pairs of opening and closing brackets
            '(': ')',
            '{': '}',
            '[': ']'
        };

        for (let i = 0; i < s.length; i++) {
            const char = s[i]; // Get the current character

            if (pairs[char]) { // If the character is an opening bracket
                stack.push(char); // Push it onto the stack
            } else { // If the character is a closing bracket
                if (stack.length === 0 || pairs[stack.pop()] !== char) {
                    // If the stack is empty or the top of the stack doesn't match the current closing bracket
                    return false; // Return false, as the string is invalid
                }
            }
        }

        return stack.length === 0; // Return true if the stack is empty (all brackets are closed), false otherwise
    }
}