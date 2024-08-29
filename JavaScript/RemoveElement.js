/**
 * Removes all occurrences of a given value from an array in-place.
 * The order of the elements may be changed.
 * Returns the number of elements in the array that are not equal to the given value.
 *
 * @param {number[]} nums - The input array of numbers.
 * @param {number} val - The value to be removed from the array.
 * @returns {number} - The number of elements in the array that are not equal to the given value.
 */
function removeElement(nums, val) {
    let k = 0;
    for (let i = 0; i < nums.length; i++) { // Iterate through the array
        if (nums[i] !== val) { // If the current element is not equal to the value
            nums[k] = nums[i]; // Copy the current element to the k-th position
            k++;
        }
    }
    return k; // Return the number of elements that are not equal to the value
}