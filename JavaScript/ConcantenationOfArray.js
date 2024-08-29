/**
 * Concatenates the given array with itself.
 * 
 * @param {number[]} nums - The input array of integers.
 * @returns {number[]} - The concatenated array.
 */
function getConcatenation(nums) {
    const n = nums.length; //Gets the length of the array
    const ans = new Array(2 * n); //Creates a new array with double the length of the input array
    
    for (let i = 0; i < n; i++) {
        ans[i] = nums[i]; //Copies the elements of the input array to the new array
        ans[i + n] = nums[i]; //Copies the elements of the input array to the new array
    }
    
    return ans;
}